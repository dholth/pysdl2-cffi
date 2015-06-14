"""
Detect the currently available SDL2 version without using the full
pysdl2-cffi binding.
"""

from __future__ import print_function
import ctypes.util, cffi

ffi = cffi.FFI()

ffi.cdef("""
typedef struct SDL_version
{
    uint8_t major;
    uint8_t minor;
    uint8_t patch;
} SDL_version;
extern void SDL_GetVersion(SDL_version * ver);
        """)

lib = ffi.dlopen(ctypes.util.find_library("SDL2"))

def getVersion():
    version = ffi.new("SDL_version *")
    lib.SDL_GetVersion(version)
    return (version.major, version.minor, version.patch)

if __name__ == "__main__":
    print(getVersion())
