from ast import *

try:
    TryExcept
except NameError:
    TryExcept = Try # Python 3

def struct_def(name, docstring, c_name, fields):
    return ClassDef(name=name, bases=[Name(id='Struct')],
        body=[Expr(value=Str(s=docstring)),
            Assign(targets=[Name(id='__ctype__')],
                value=Str(s=c_name)),
            Assign(targets=[Name(id='_fields')],
                value=Tuple(elts=[Str(s=field) for field in fields])),
            ],
        decorator_list=[])

def struct_plain_field(name):
    """
    Handle a field that does not require extra cffi translation (int, etc.)
    """
    return [
        FunctionDef(name=name,
            args=arguments(args=[Name(id='self')], vararg=None, kwarg=None, defaults=[]),
            body=[Return(value=Attribute(value=Attribute(value=Name(id='self'), attr='cdata'), attr=name))],
            decorator_list=[Name(id='property')]),
        FunctionDef(name=name,
            args=arguments(args=[Name(id='self'), Name(id='value')], vararg=None, kwarg=None, defaults=[]),
            body=[
                Assign(
                    targets=[Attribute(value=Attribute(value=Name(id='self'), attr='cdata'), attr=name)],
                    value=Name(id='value'))],
            decorator_list=[Attribute(value=Name(id=name), attr='setter')]),
        ]

def struct_boxed_field(name, wrapper_class_name, c_type):
    """
    Handle a field that has to be boxed/unboxed (SDL_Rect etc.)
    """
    return [
        FunctionDef(name=name,
            args=arguments(args=[Name(id='self')], vararg=None, kwarg=None, defaults=[]),
            body=[
                Return(
                    value=IfExp(
                        test=Attribute(value=Attribute(value=Name(id='self'), attr='cdata'), attr=name),
                        body=Call(func=Name(id=wrapper_class_name),
                            args=[Attribute(value=Attribute(value=Name(id='self'), attr='cdata'), attr=name)],
                            keywords=[],
                            starargs=None,
                            kwargs=None),
                        orelse=Name(id='None')))],
            decorator_list=[Name(id='property')]),
        FunctionDef(name=name,
            args=arguments(args=[Name(id='self'), Name(id='value')], vararg=None, kwarg=None, defaults=[]),
            body=[
                TryExcept(
                    finalbody=None,
                    body=[
                        Assign(
                            targets=[
                                Attribute(value=Attribute(value=Name(id='self'), attr='cdata'),
                                    attr=name)],
                            value=Attribute(value=Name(id='value'), attr='cdata'))],
                    handlers=[
                        ExceptHandler(type=None,
                            name=None,
                            body=[
                                Assign(
                                    targets=[
                                        Attribute(value=Attribute(value=Name(id='self'), attr='cdata'),
                                            attr=name)],
                                    value=Call(func=Attribute(value=Name(id='ffi'), attr='new'),
                                        args=[Str(s=c_type + ' *'), Name(id='value')],
                                        keywords=[],
                                        starargs=None,
                                        kwargs=None))])],
                    orelse=[])],
            decorator_list=[Attribute(value=Name(id=name), attr='setter')])]


