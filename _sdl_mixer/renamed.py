# "pretty" names without the NAMESPACE_ prefixes...
from __future__ import absolute_import

import _sdl.renamer

__all__ = []

def _get_renamer():
    import re
    constant_re = re.compile("MIX_(?P<pretty_name>[A-Z][A-Z].+)$")
    renamer = _sdl.renamer.Renamer(None, 'Mix_', constant_re)
    return renamer

def _mapping():
    from _sdl_mixer import lib
    renamer = _get_renamer()
    for name in dir(lib):
        value = getattr(lib, name)
        pretty_name = renamer.rename(name, value)
        if not pretty_name:
            continue
        yield name, pretty_name

def _init():
    from _sdl_mixer import lib
    here = globals()
    for name, pretty_name in _mapping():
        here[pretty_name] = getattr(lib, name)
        __all__.append(pretty_name)
    __all__.sort()

# _init()
