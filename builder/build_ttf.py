# Generate SDL_image wrappers.
# Only used at build time.

import os
import re

from .builder import Builder

header = """# Automatically generated wrappers.
# Override by adding wrappers to helpers.py.
from __sdl_ttf import ffi, lib
from _sdl_ttf.structs import unbox, Struct
from _sdl.structs import u8, SDLError
# ttf needs the aliases for now...
from sdl import Surface as SDL_Surface, version as SDL_version

"""

def go():
    from _sdl_ttf import cdefs, renamed
    builder = Builder(renamer=renamed._get_renamer())
    output_filename = os.path.join(os.path.dirname(__file__),
                                   "..",
                                   "sdl", "ttf.py")
    with open(output_filename, "w+") as output:
        output.write(header)
        builder.generate(output,
                         cdefs=cdefs,
                         helpers=cdefs,
                         filter=re.compile("^.* TTF_.*$"))

if __name__ == "__main__":
    go()
