# Quick, dirty way to generate wrapper functions by iterating over cffi's
# parsed declarations.

import os.path
import cffi.model
import collections

def is_primitive(arg):
    """Return true if arg is primitive or primitive*"""
    if hasattr(arg, 'totype'):
        arg = arg.totype # a pointer
    if hasattr(arg, 'ALL_PRIMITIVE_TYPES') and \
        arg.get_c_name() in arg.ALL_PRIMITIVE_TYPES:
        print "primitive %s" % (arg.get_c_name())
        return True
    print "not primitive %s" % (arg.get_c_name())
    return False

def treatment(name, declaration):
    for i, arg in enumerate(declaration.args):
        c_name = arg.get_c_name()
        if is_primitive(arg):
            yield ('pass', arg, None)
        elif i == 0 and c_name.startswith("SDL_") and c_name.endswith('*'):
            yield ('self', arg, None)
        elif c_name.endswith('*'):
            yield ('new', arg, True)
        else:
            yield('', arg, None)

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

def handle_enum(output, declaration_name, declaration):
    if not hasattr(declaration, "enumerators"):
        # it might be an anonymous struct
        return
    for name in declaration.enumerators:
        output.writeln("%s = _LIB.%s" % (name, name))
    output.writeln("")

declarations_by_type = collections.defaultdict(list)

def handle_struct(output, declaration_name, declaration):
    output.writeln("class %s(Struct):" % declaration.name)
    output.indent()
    functions = declarations_by_type[declaration.name + " *"]
    for fname in functions:
        short_name = fname[4].lower() + fname[5:]
        output.writeln("%s = %s" % (short_name, fname))
    if not functions:
        output.writeln("pass")
    output.dedent()
    output.writeln("")

STRING_TYPES = ["char *", "char const *"]

def handle_function(output, declaration_name, declaration):
    fname = declaration_name.split(' ')[1]

    returns_void = isinstance(declaration.result, cffi.model.VoidType)

    if declaration.args:
        declarations_by_type[declaration.args[0].get_c_name()].append(fname)

    arg_names  = ["a%d" % i for i in range(len(declaration.args))]
    arg_vars = ', '.join(arg_names)
    output.writeln("def %s(%s):" % (fname, arg_vars))
    output.indent()
    output.writeln('"""' + declaration.get_c_name().replace("(*)", " " + fname) + '"""')

    line = []
    if not returns_void:
        line.append("rc =")
    line.append("_LIB.%s(%s)" % (fname,
                                 ', '.join(["unbox(%s)" % name
                                 for name in arg_names])))
    output.writeln(" ".join(line))

    if returns_void:
        pass
    elif declaration.result.get_c_name() in STRING_TYPES:
        output.writeln("return ffi.string(rc)")
    else:
        output.writeln("return rc")
    output.dedent()
    output.writeln("")

    return

    returning = []
    for i, (action, arg, returns) in enumerate(treatment(fname, declaration)):
        if action in ("pass", "self"):
            output.writeln("c_args[%d] = args[%d]" % (i, i))
        elif action == "new":
            output.writeln("c_args[%d] = ffi.new(%s)" % (i, repr(arg.get_c_name())))

            if returns:
                if isinstance(arg.totype, cffi.model.StructType):
                    # later, wrap structs.
                    returning.append("c_args[%d]" % (i,))
                else:
                    returning.append("c_args[%d][0]" % (i,))

        else:
            output.writeln("c_args[%d] = None" % (i, ))

    output.writeln("rc = _LIB.%s(*c_args)" % (fname,))

    if not returning:
        if declaration.result.get_c_name() == "char *":
            output.writeln("return ffi.string(rc)")
        else:
            output.writeln("return rc")
    else:
        if len(returning) == 1:
            output.writeln("return %s" % returning[0])
        else:
            output.writeln("return (" + ", ".join(returning) + ")")

    output.dedent()
    output.writeln("")

def get_declarations(ffi):
    return ffi._parser._declarations

def generate(output,
             cdefs=None,
             helpers=None,
             filter=None):
    """
    Automatically generate libSDL2 wrappers by following some simple rules.
    Only used during build time.
    """
    sort_order = {'anonymous' : 4,
                  'function' : 1,
                  'struct' : 2,
                  'union' : 3 }

    def sort_key(declaration_name):
        kind, name = declaration_name.split()
        return (sort_order.get(kind, kind), name)

    declarations = get_declarations(cdefs.ffi)
    output = IndentedWriter(output)
    for declaration_name in sorted(declarations, key=sort_key):
        if filter and not filter.match(declaration_name):
            continue
        declaration_kind, declaration_n = declaration_name.split(" ")
        if declaration_kind == "function":
            handle_function(output,
                declaration_name,
                declarations[declaration_name])

        elif declaration_kind in ("struct", "union"):
            handle_struct(output,
                declaration_name,
                declarations[declaration_name])

        elif declaration_kind in ("anonymous",):
            handle_enum(output,
                        declaration_name,
                        declarations[declaration_name])

        else:
            print(declaration_name)

        # XXX do something about typedefs that are the friendly struct names

        continue

        # XXX unreachable code:
        # The below may become a higher-level wrapper:

        fname = declaration_name.split(' ')[1]

        # Skip manually written helpers:
        if hasattr(helpers, fname):
            continue

        declaration = declarations[declaration_name]

        if declaration.args:
            output.writeln("def %s(*args):" % fname)
        else:
            output.writeln("def %s():" % fname)

        output.indent()
        output.writeln('"""' + declaration.get_c_name().replace("(*)", " " + fname) + '"""')
        output.writeln("c_args = %s" % (repr([None]*len(declaration.args))))

        returning = []
        for i, (action, arg, returns) in enumerate(treatment(fname, declaration)):
            if action in ("pass", "self"):
                output.writeln("c_args[%d] = args[%d]" % (i, i))
            elif action == "new":
                output.writeln("c_args[%d] = ffi.new(%s)" % (i, repr(arg.get_c_name())))

                if returns:
                    if isinstance(arg.totype, cffi.model.StructType):
                        # later, wrap structs.
                        returning.append("c_args[%d]" % (i,))
                    else:
                        returning.append("c_args[%d][0]" % (i,))

            else:
                output.writeln("c_args[%d] = None" % (i, ))

        output.writeln("rc = _LIB.%s(*c_args)" % (fname,))

        if not returning:
            if declaration.result.get_c_name() == "char *":
                output.writeln("return ffi.string(rc)")
            else:
                output.writeln("return rc")
        else:
            if len(returning) == 1:
                output.writeln("return %s" % returning[0])
            else:
                output.writeln("return (" + ", ".join(returning) + ")")

        output.dedent()
        output.writeln("")

header = """# Automatically generated wrappers.
# Override by adding wrappers to helpers.py.
from .dso import ffi, _LIB
from .structs import Struct, unbox

"""

api = ["""# API
import apipkg

exports = """, """

ns_dict = dict((s, '_sdl.renamed:%s' % s)
               for s in exports if not s.startswith('_'))
ns_dict['image'] = '_sdl_image.renamed'
ns_dict['mixer'] = '_sdl_mixer.renamed'

apipkg.initpkg(__name__, ns_dict)
"""]

def go():
    from . import cdefs, helpers

    output_filename = os.path.join(os.path.dirname(__file__), "autohelpers.py")
    with open(output_filename, "w+") as output:
        output.write(header)
        generate(output, cdefs=cdefs, helpers=helpers)

    import pprint
    import _sdl.renamed
    exports = pprint.pformat(sorted(dir(_sdl.renamed)))
    api_filename = os.path.join(os.path.dirname(__file__), "..", "sdl", "__init__.py")
    with open(api_filename, "w+") as output:
        output.write(exports.join(api))

if __name__ == "__main__":
    go()
