"""
Call cffi to compile the extension module.
With cffi 1.0 this is only needed at build time.
"""

import cffi
ffi = cffi.FFI()
import os.path

here = os.path.dirname(__file__)
for filename in ("sdl.h", "defines.h"):
    with open(os.path.join(here, filename), "r") as header:
        ffi.cdef(header.read())

ffi.set_source("__sdl", 
    """
    #include <SDL2/SDL.h>
    """,
    libraries=["SDL2"])
    
if __name__ == "__main__":
    ffi.compile()
