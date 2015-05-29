#!/bin/sh
# Generate automatic wrapper helpers.
(cd builder ; python dox.py ~/prog/SDL2-2.0.3/include/xml/)
# Compile all of the extension modules
python -m _sdl.cdefs
python -m _sdl_image.cdefs
python -m _sdl_mixer.cdefs
python -m _sdl_ttf.cdefs
# Build the API wrappers
python -m builder.build_sdl
python -m builder.build_ttf
python -m builder.build_mixer
python -m builder.build_image
# Build the friendly sdl API
python -m builder.build_api
# Sphinx and doc extraction don't work in Python 3 yet.
echo "Sphinx"
(cd docs; make clean; make html)
