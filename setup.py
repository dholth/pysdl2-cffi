#!/usr/bin/env python

from setuptools import setup

setup(name="pysdl2-cffi",
	packages = [ 'sdl', '_sdl' ],
	install_requires = [ 'cffi' ],
	summary = "SDL2 wrapper with cffi")
