# "pretty" names without the NAMESPACE_ prefixes...
from __future__ import absolute_import

import _sdl.renamer
from _sdl_ttf import lib

__all__ = []

def _init():
    here = globals()
    import re
    constant_re = re.compile("TTF_(?P<pretty_name>[A-Z][A-Z].+)$")
    renamer = _sdl.renamer.Renamer(lib, "TTF_", constant_re)
    for name in dir(lib):
        value = getattr(lib, name)
        pretty_name = renamer.rename(name, value)
        if not pretty_name:
            continue
        here[pretty_name] = value
        __all__.append(pretty_name)
        __all__.sort()

_init()