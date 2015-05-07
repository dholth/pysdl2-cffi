import cffi
ffi = cffi.FFI()
import os.path

if __name__ == "__main__":
    sdl_h = open(os.path.join(os.path.dirname(__file__), "sdl.h"), "r").read()
    ffi.cdef(sdl_h)
    ffi.set_source("__sdl", """
    #include <SDL2/SDL.h>
    """,
    libraries=["SDL2"])
    ffi.compile()
