# "pretty" names without the NAMESPACE_ prefixes...
from __future__ import absolute_import

import _sdl.renamer

__all__ = []

def _get_renamer():
    import re
    constant_re = re.compile("IMG_(?P<pretty_name>[A-Z][A-Z].+)$")
    renamer = _sdl.renamer.Renamer(None, "IMG_", constant_re)
    return renamer

def _mapping():
    from . import lib
    import re
    renamer = _get_renamer()
    constant_re = re.compile("IMG_[A-Z][A-Z]+")
    for name in dir(lib):
        if not name.startswith("IMG_"):
            continue
        elif constant_re.match(name):
            pretty_name = name[4:]
        else:
            pretty_name = name[4].lower() + name[5:]
        yield name, pretty_name

def _init():
    from . import lib
    here = globals()
    for name, pretty_name in _mapping():
        here[pretty_name] = getattr(lib, name)
        __all__.append(pretty_name)
    __all__.sort()

# _init()
