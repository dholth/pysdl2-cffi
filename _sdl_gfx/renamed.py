# "pretty" names without the NAMESPACE_ prefixes...
# (sdl2_gfx does not use prefixes)
from __future__ import absolute_import

__all__ = []

def _get_renamer():
    import re
    constant_re = re.compile("IMG_(?P<pretty_name>[A-Z][A-Z].+)$")
    renamer = _sdl.renamer.Renamer(None, "IMG_", constant_re)
    return renamer

def _mapping():
    from . import lib
    renamer = _get_renamer()
    for name in dir(lib):
        yield name, name
        
def _init():
    from . import lib
    here = globals()
    for name, pretty_name in _mapping():
        here[pretty_name] = getattr(lib, name)
        __all__.append(pretty_name)
    __all__.sort()

# _init()
