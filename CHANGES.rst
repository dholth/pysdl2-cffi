0.9.0
-----
- ``sdl.*`` bindings are generated directly instead of using apipkg. Works
  better with IDE autocomplete. Now you have to import sdl.image, sdl.mixer,
  sdl.ttf separately instead of just ``import sdl`` to use image, mixer,
  ttf libraries.
- _sdl.lib.SDL_* (non-renamed) wrappers have been removed. The raw cffi
  functions are still available in __sdl.lib, __sdl_image.lib etc.
- SDL math and string functions have been removed. Use the Python equivalents.
- __str__ representation of all structs.
  >>> print(sdl.Rect((0,0,12,42)))
  <Rect x=0 y=0 w=12 h=42>
- Struct properties return and accept wrapper classes instead of raw
  cffi objects in many places. 
  ``isinstance(sdl.Surface().clip_rect, sdl.Rect) == True`` 
  Lessens the need to use lower-level cffi functions.
- ``sdl.Event().unwrapEvent()`` added to convert a generic event into the 
  correct union member e.g. ``WindowEvent``, ``KeyboardEvent``, ...

0.8.0
-----
- Updated for cffi 1.0. Uses a compiled extension instead of dlopen. Much 
  faster on CPython.
- Can automatically grab SDL2 dependencies on Windows.

0.7.0
-----
- Struct wrappers now expose all the attributes of the C-level struct as 
  properties. Great for tinkering, as the property names can now be 
  inspected interactively.
- Struct wrappers no longer pass all attribute access through
  getattr/setattr. Arbitrary data can be attached to the struct wrappers
  as is customary in Python.
- Fix a capitalization error for the "classy" API to conform to the general
  binding rules. ``ob.gL_Function`` is now ``ob.GL_Function``.

0.6.0
-----
- Windows is now supported! You must manually download the SDL2 dll's and
  place them on PATH ``set PATH=%PATH%;C:\users\me\SDL2Dir`` but pysdl2-cffi
  will attempt to load the Windows ``.dll`` as well as the Unix ``.so``.

0.5.1
-----
- Enums are no longer wrapped in (nonexistent) classes
- Python 2 can also pass Unicode where char* is required; automatically
  encoded to utf-8.
