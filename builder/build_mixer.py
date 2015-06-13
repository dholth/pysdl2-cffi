# Generate SDL_image wrappers.
# Only used at build time.

import os
import re
from .builder import Builder

header = """# Automatically generated wrappers.
# Override by adding wrappers to helpers.py.
from __sdl_mixer import ffi, lib
from _sdl_mixer.structs import unbox, Struct
from _sdl.structs import u8

# alias needed here
from sdl import version as SDL_version

# helpers (from C macros)
def playChannel(channel, chunk, loops):
    return playChannelTimed(channel, chunk, loops, -1)

def loadWAV(file):
    return loadWAV_RW(sdl.RWFromFile(file, b"rb"), 1)

def fadeInChannel(channel,chunk,loops,ms):
    return fadeInChannelTimed(channel,chunk,loops,ms,-1)

"""

def go():
    from _sdl_mixer import cdefs, renamed
    builder = Builder(renamer=renamed._get_renamer())
    output_filename = os.path.join(os.path.dirname(__file__),
                                   "..",
                                   "sdl", "mixer.py")
    with open(output_filename, "w+") as output:
        output.write(header)
        builder.generate(output,
                         cdefs=cdefs,
                         helpers=cdefs,
                         filter=re.compile("^.* (Mix_|MIX_).*$"))

if __name__ == "__main__":
    go()
