# Generate SDL_image wrappers.
# Only used at build time.

import os
import re
from _sdl import builder

header = """# Automatically generated wrappers.
# Override by adding wrappers to helpers.py.
from .dso import ffi, _LIB
from _sdl.structs import unbox, Struct

"""

def go():
    from _sdl_mixer import cdefs
    output_filename = os.path.join(os.path.dirname(__file__), "autohelpers.py")
    with open(output_filename, "w+") as output:
        output.write(header)
        builder.generate(output,
                         cdefs=cdefs,
                         helpers=cdefs,
                         filter=re.compile("^.* (Mix_|MIX_).*$"))

if __name__ == "__main__":
    go()
