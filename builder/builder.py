# Quick, dirty way to generate wrapper functions by iterating over cffi's
# parsed declarations.

import cffi.model
import collections
import re
import types

types.TypeType = type

from ast import *
import astor

from .handle_struct import struct_def, struct_plain_field, struct_boxed_field

# get the pycparser that cffi is using
import cffi.cparser
Decl = cffi.cparser.pycparser.c_ast.Decl
FuncDecl = cffi.cparser.pycparser.c_ast.FuncDecl

from . import errorprone, nullable

def is_primitive(arg):
    """Return True if arg is primitive"""
    primitive = False
    if hasattr(arg, 'ALL_PRIMITIVE_TYPES') and arg.get_c_name() in arg.ALL_PRIMITIVE_TYPES:
        primitive = True
    return primitive

def is_direct(arg):
    """Return True if arg can be handled directly by cffi."""
    return (is_primitive(arg) or
            (getattr(arg, 'kind', '') == 'enum'))

def is_utf8(arg):
    """
    Return True if arg should be utf8.

    TODO figure out which char* are not utf8.
    """
    if (arg.get_c_name() in ('char *', 'char const *')):
        return True
    return False

def is_primitive_or_primitive_p(arg):
    """Return True if arg is primitive or primitive*"""
    if hasattr(arg, 'totype'):
        arg = arg.totype  # a pointer
    primitive = is_primitive(arg)
    return primitive

def is_primitive_p(arg):
    """Return True if arg is primitive*"""
    return is_primitive_or_primitive_p(arg) and hasattr(arg, 'totype')

def is_struct_p(fldtype):
    return (getattr(fldtype, 'totype', '') 
            and getattr(fldtype.totype, 'kind', '') == 'struct') \
                    and not 'struct' in fldtype.totype.get_c_name()

def get_base_name(c_type):
    c_name = c_type.get_c_name()
    match = re.match('(\w+_\w+)( const)?( *)', c_name)
    assert match, c_name
    if match:
        return match.group(1)

class IndentedWriter(object):
    def __init__(self, writer):
        self.writer = writer
        self.level = 0
        self.indentation = "    "

    def writeln(self, msg):
        self.writer.write(self.indentation * self.level)
        self.writer.write(msg)
        self.writer.write("\n")

    def indent(self):
        self.level += 1

    def dedent(self):
        self.level -= 1

def iter_declarations(ffi):
    """Yield all declarations from an ffi object."""
    # Sometimes the source is a square bracket... related to ffi.include?
    for source in ffi._cdefsources:
        if source in '[]': continue
        ast = ffi._parser._parse(source)[0]
        for _, node in ast.children():
            if not isinstance(node, Decl):
                continue
            yield node

def get_declarations(ffi):
    return ffi._parser._declarations

def get_outargs(declaration):
    """
    Guess which arguments are output parameters by finding all primitive
    arguments at the end of a function's argument list.
    """
    outargs = {}
    for i in range(len(declaration.args) - 1, -1, -1):
        arg = declaration.args[i]
        if not is_primitive_p(arg):
            break
        if arg.get_c_name() in STRING_TYPES:
            break
        outargs[i] = arg
    return outargs

def funcnames_argnames(declarations):
    """
    Yield (function name, function argument names) for all functions in
    declarations.

    Some functions have parameters named None. This is either the void
    parameter or an unnamed parameter.
    """
    for declaration in declarations:
        if not isinstance(declaration.type, FuncDecl):
            continue
        funcname = declaration.name
        funcargs = list(p.name for p in declaration.type.args.params)
        for i, arg in enumerate(funcargs):
            if arg in ('from',):  # pesky Python keywords
                funcargs[i] = funcargs[i] + '_'
        yield funcname, funcargs

STRING_TYPES = ["char *", "char const *"]

class Builder(object):
    """
    Generate wrapper helpers based on some simple rules.
    """
    def __init__(self, funcdocs={}, renamer=None):
        """
        :param funcdocs: dict of {function name: docstring}.
        :param renamer: _sdl.renamer.Renamer
        """
        self.all_funcdocs = funcdocs
        self.declarations_by_type = collections.defaultdict(list)

        self.renamer = renamer

    def handle_enum(self, output, declaration_name, declaration):
        if not hasattr(declaration, "enumerators"):
            # it might be an anonymous struct
            return
        for name in declaration.enumerators:
            py_name = self.renamer.rename(name)
            output.writeln("%s = lib.%s" % (py_name, name))
        output.writeln("")
        
    def handle_macro(self, output, name, declaration):
        py_name = self.renamer.rename(name)
        output.writeln("%s = lib.%s" % (py_name, name))
        output.writeln("")

    def handle_struct_ast(self, output, declaration_name, declaration):
        c_name = declaration.get_c_name()
        py_name = self.renamer.rename(c_name, type)
        struct = struct_def(py_name, "Wrap `%s`" % c_name, c_name, declaration.fldnames or [])

        def handle_fields():
            for i, (fldname, fldtype) in enumerate(zip(declaration.fldnames, 
                declaration.fldtypes)):

                if fldtype.has_c_name():
                    fld_c_name = fldtype.get_c_name()
                else:
                    print("XXX", declaration, fldname, fldtype.has_c_name())
                    fld_c_name = None

                if (is_direct(fldtype) 
                        or not fld_c_name 
                        or fld_c_name == 'void *'):
                    struct.body.extend(struct_plain_field(fldname))
                elif hasattr(fldtype, 'item'):
                    print(declaration, "Has item", i, fldname, fldtype)
                    struct.body.extend(struct_plain_field(fldname))
                elif not is_primitive_or_primitive_p(fldtype):
                    try:
                        base_name = get_base_name(fldtype)
                        field_py_name = self.renamer.rename(base_name, types.TypeType)
                        struct.body.extend(struct_boxed_field(fldname, field_py_name, base_name))
                    except Exception as e:
                        # Mostly function pointers
                        print(declaration, "Exception", i, fldname, e)
                        struct.body.extend(struct_plain_field(fldname))
                        # some of these may by read-only
                else:
                    print(declaration, "Unhandled", c_name, fldname, fldtype)
                    struct.body.extend(struct_plain_field(fldname))

        # Add @property wrappers for fields
        if declaration.fldnames:
            handle_fields()

        # Add associated functions to struct:
        functions = self.declarations_by_type[c_name + " *"]
        for fname in functions:
            short_name = self.renamer.rename(fname, None)
            struct.body.append(Assign(targets=[Name(id=short_name)], value=Name(id=short_name)))

        return astor.to_source(struct)

    def handle_function(self,
                        output,
                        declaration_name,
                        declaration,
                        arg_names):
        fname = declaration_name.split(' ')[1]
        py_name = self.renamer.rename(fname)

        if declaration.args:
            # take 'const' out of c name for this purpose.
            first_arg_name = declaration.args[0].get_c_name().replace('const ', '')
            self.declarations_by_type[first_arg_name].append(fname)

        outargs = get_outargs(declaration)

        # XXX filtering out the None parameter. Many of these are varargs functions
        # or logging functions that may not be necessary in our wrapper...
        # Later, compare to declaration.args, filter out void, and make names
        # for the varargs parameters.
        arg_names = list(name for name in arg_names if name)

        def arg_names_with_defaults():
            """
            Default primitive out-parameters to None, so cffi can allocate a
            new one to be returned.
            """
            for i, arg_name in enumerate(arg_names):
                if i in outargs:
                    yield "%s=None" % arg_name
                else:
                    yield arg_name

        arg_vars = ', '.join(arg_names_with_defaults())
        output.writeln("def %s(%s):" % (py_name, arg_vars))
        output.indent()
        docstring = declaration.get_c_name().replace("(*)", " " + fname)
        output.writeln('"""')
        output.writeln("``" + docstring + "``")
        if fname in self.all_funcdocs:
            for doc_line in self.all_funcdocs[fname].splitlines():
                output.writeln(doc_line.rstrip())
        output.writeln('"""')

        for i, arg in enumerate(arg_names):
            c_arg = declaration.args[i]
            c_name = c_arg.get_c_name()
            if is_direct(c_arg):  # directly handled by cffi
                output.writeln("%s_c = %s" % (arg, arg))
            elif is_utf8(c_arg):
                output.writeln('%(arg)s_c = u8(%(arg)s)' % dict(arg=arg))
            else:
                null_ok = nullable.nullable.get(fname, ())
                output.writeln('%(arg)s_c = unbox(%(arg)s, %(c_name)r%(null_ok)s)' %
                               (dict(arg=arg, c_name=c_name,
                                     null_ok=(', nullable=True' if arg in null_ok else ''))))

        line = []
        returns_void = isinstance(declaration.result, cffi.model.VoidType)
        if not returns_void:
            line.append("rc =")
        line.append("lib.%s(%s)" % (fname, ', '.join("%s_c" % arg for arg in arg_names)))
        output.writeln(" ".join(line))

        # handle errors
        error_handler = errorprone.handler_for_function(fname)
        if error_handler:
            output.writeln(error_handler)

        returning = []
        result_name = declaration.result.get_c_name()
        if returns_void:
            pass
        elif result_name in STRING_TYPES:
            returning.append("ffi.string(rc).decode('utf-8')")
        elif (result_name in ("void *", "struct _SDL_iconv_t *") or
              is_direct(declaration.result)):
            returning.append("rc")
        elif not is_primitive_or_primitive_p(declaration.result):
            match = re.match('(\w+_\w+)( const)?( *)', result_name)
            assert match
            if match:
                rc_py_name = self.renamer.rename(match.group(1), types.TypeType)
                returning.append("%s(rc)" % rc_py_name)
        else:
            returning.append("rc")

        for i, arg in enumerate(arg_names):
            # Assume all out-parameters are like int*, a single element.
            if i in outargs:
                returning.append("%s_c[0]" % arg)

        if len(returning) == 1:
            output.writeln("return %s" % returning[0])
        elif len(returning) > 1:
            output.writeln("return (%s)" % ", ".join(returning))

        output.dedent()
        output.writeln("")

    def generate(self,
                 output,
                 cdefs=None,
                 filter=None):
        """
        Automatically generate libSDL2 wrappers by following some simple rules.
        Only used during build time.
        """
        sort_order = {'anonymous' : 3,
                      'macro' : 4,
                      'function' : 0,
                      'struct' : 1,
                      'union' : 2,                      
                      'typedef' : 5 }

        # 'macro' for #defines

        argument_names = dict(funcnames_argnames(iter_declarations(cdefs.ffi)))

        def sort_key(declaration_name):
            kind, name = declaration_name.split()
            return (sort_order.get(kind, kind), name)

        declarations = get_declarations(cdefs.ffi)
        output = IndentedWriter(output)
        for declaration_name in sorted(declarations, key=sort_key):
            declaration = declarations[declaration_name][0]
            if filter and not filter.match(declaration_name):
                continue
            declaration_kind, declaration_n = declaration_name.split(" ")

            if declaration_kind == "function":
                self.handle_function(output,
                    declaration_name,
                    declaration,
                    argument_names[declaration_n])

            elif (declaration_kind == "typedef" and
                  hasattr(declaration, 'kind') and
                  declaration.kind in ("struct", "union")):
                output.writeln(self.handle_struct_ast(output,
                    declaration_name,
                    declaration))

            elif declaration_kind in ("anonymous",):
                self.handle_enum(output,
                            declaration_name,
                            declaration)

            elif declaration_kind == "macro":
                self.handle_macro(output, declaration_n, declaration)
