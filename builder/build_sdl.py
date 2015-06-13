# Generate libSDL2 wrappers.

import json
import os.path

from .builder import Builder

header = """# Automatically generated wrappers.
# Override by adding wrappers to helpers.py.
from __sdl import ffi, lib
from _sdl.structs import Struct, unbox, SDLError, u8
from _sdl.helpers import *

import _sdl.pixels
import _sdl.constants

for _lib in _sdl.pixels, _sdl.constants:
    globals().update(dict((key[4:], getattr(_lib, key)) 
        for key in dir(_lib) if key.startswith('SDL_')))

"""

footer = """blitSurface = upperBlit

# Must import after definitions due to circular dependencies
try:
    import sdl.image, sdl.ttf, sdl.mixer
except ImportError:
    pass
"""

def go():
    import _sdl.renamed
    from _sdl import cdefs, helpers

    try:
        with open(os.path.join(os.path.dirname(__file__), 'dox.json'), 'r') as funcdocs:
            all_funcdocs = json.load(funcdocs)
    except IOError:
        all_funcdocs = {}

    renamer = _sdl.renamed._get_renamer()
    builder = Builder(all_funcdocs, renamer)
    # pure-Python helpers/additional methods:
    builder.declarations_by_type['SDL_Event *'] = ['unwrapEvent']

    output_filename = os.path.join(os.path.dirname(__file__),
                                   "..",
                                   "sdl",
                                   "__init__.py")
    with open(output_filename, "w+") as output:
        output.write(header)
        builder.generate(output, cdefs=cdefs, helpers=helpers)
        output.write(footer)

if __name__ == "__main__":
    go()
