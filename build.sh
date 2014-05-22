#!/bin/sh
# Generate automatic wrapper helpers.
python -m _sdl.builder
python -m _sdl_image.builder
python -m _sdl_mixer.builder
