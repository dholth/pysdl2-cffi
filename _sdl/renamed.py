# "pretty" names without the NAMESPACE_ prefixes...
from __future__ import absolute_import

import _sdl.renamer

__all__ = []

def _get_renamer():
    import re
    whitelist = ['SDLError', 'Struct', 'ffi']
    constant_re = re.compile("(SDL_)(?P<pretty_name>[A-Z][A-Z].+)$")
    renamer = _sdl.renamer.Renamer(None, "SDL_", constant_re, whitelist)
    return renamer

def _mapping():
    from . import lib
    # as an alternative, these names could go straight into sdl/__init__.py
    # allowed even though they don't start with prefix:
    renamer = _get_renamer()
    for name in dir(lib):
        value = getattr(lib, name)
        pretty_name = renamer.rename(name, value)
        if not pretty_name:
            continue
        yield name, pretty_name

def _init():
    from . import lib
    # XXX use apipkg here?
    here = globals()
    for name, pretty_name in _mapping():
        here[pretty_name] = getattr(lib, name)
        __all__.append(pretty_name)
    __all__.sort()

# _init()
