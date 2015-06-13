# Generate SDL_image wrappers.
# Only used at build time.

import os
import re

from .builder import Builder

header = """# Automatically generated wrappers.
# Override by adding wrappers to helpers.py.
from __sdl_image import ffi, lib
from _sdl_image.structs import unbox
from _sdl.structs import SDLError, u8

from sdl import Surface as SDL_Surface, Texture as SDL_Texture, version as SDL_version
from sdl import getError, setError

"""

def go():
    from _sdl_image import cdefs, renamed
    builder = Builder(renamer=renamed._get_renamer())
    output_filename = os.path.join(os.path.dirname(__file__),
                                   "..",
                                   "sdl", "image.py")
    with open(output_filename, "w+") as output:
        output.write(header)
        builder.generate(output,
                         cdefs=cdefs,
                         helpers=cdefs,
                         filter=re.compile("^.* IMG_.*$"))

if __name__ == "__main__":
    go()
