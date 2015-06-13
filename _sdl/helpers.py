# Handwritten helper methods for those hard-to-wrap functions.
# Overrides same-named functions from autohelpers.py

from __sdl import ffi, lib
from .structs import unbox

def calculateGammaRamp(a0, a1=ffi.NULL):
    """void SDL_CalculateGammaRamp(float, uint16_t *)

    :param gamma: a gamma value where 0.0 is black and 1.0 is identity
    :param ramp: an array of 256 values filled in with the gamma ramp
    :return: ramp
    """
    if a1 == ffi.NULL:
        a1 = ffi.new("uint16_t[]", 256)
    lib.SDL_CalculateGammaRamp(a0, a1)
    return a1

def joystickGetGUIDString(a0):
    """
    ``void SDL_JoystickGetGUIDString(SDL_JoystickGUID, char *, int)``

    Return a string representation for this guid. pszGUID must point to at
    least 33 bytes (32 for the string plus a NULL terminator).
    """
    buf = ffi.new('char *', 33)
    lib.SDL_JoystickGetGUIDString(unbox(a0), buf, 33)
    return ffi.string(buffer)

def loadBMP(file):
    return lib.SDL_LoadBMP_RW(lib.SDL_RWFromFile(file, "rb"), 1)

def unwrapEvent(event):
    """Return correct union member for event.type, or just the common data if unknown."""
    return getattr(event, _event_mapping.get(event.type, 'common'))

_event_mapping_in = {
    # (lib.SDL_AUDIODEVICEADDED, lib.SDL_AUDIODEVICEREMOVED,): 'adevice', # since 2.0.4
    (lib.SDL_CONTROLLERAXISMOTION,): 'caxis',
    (lib.SDL_CONTROLLERBUTTONDOWN, lib.SDL_CONTROLLERBUTTONUP,): 'cbutton',
    (lib.SDL_CONTROLLERDEVICEADDED, 
        lib.SDL_CONTROLLERDEVICEREMOVED, 
        lib.SDL_CONTROLLERDEVICEREMAPPED,): 'cdevice',
    (lib.SDL_DOLLARGESTURE, lib.SDL_DOLLARRECORD,): 'dgesture',
    (lib.SDL_DROPFILE,): 'drop',
    (lib.SDL_FINGERMOTION, lib.SDL_FINGERDOWN, lib.SDL_FINGERUP,): 'tfinger',
    (lib.SDL_KEYDOWN, lib.SDL_KEYUP,): 'key',
    (lib.SDL_JOYAXISMOTION,): 'jaxis',
    (lib.SDL_JOYBALLMOTION,): 'jball',
    (lib.SDL_JOYHATMOTION,): 'jhat',
    (lib.SDL_JOYBUTTONDOWN, lib.SDL_JOYBUTTONUP,): 'jbutton',
    (lib.SDL_JOYDEVICEADDED, lib.SDL_JOYDEVICEREMOVED,): 'jdevice',
    (lib.SDL_MOUSEMOTION,): 'motion',
    (lib.SDL_MOUSEBUTTONDOWN, lib.SDL_MOUSEBUTTONUP,) : 'button',
    (lib.SDL_MOUSEWHEEL,) : 'wheel',
    (lib.SDL_MULTIGESTURE,) : 'mgesture',
    (lib.SDL_QUIT,) : 'quit',
    (lib.SDL_SYSWMEVENT,) : 'syswm',
    (lib.SDL_TEXTEDITING,) : 'edit',
    (lib.SDL_TEXTINPUT,) : 'text',
    (lib.SDL_USEREVENT,) : 'user',
    (lib.SDL_WINDOWEVENT,) : 'window',
}

_event_mapping = {}
def _build_mapping():
    for item in _event_mapping_in.items():
        for key in item[0]:
            _event_mapping[key] = item[1]

_build_mapping()
