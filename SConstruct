# Wheel generation from SCons.
#
# Daniel Holth <dholth@gmail.com>, 2016
#
# The MIT License
#
# Permission is hereby granted, free of charge, to any person obtaining a
# copy of this software and associated documentation files (the "Software"),
# to deal in the Software without restriction, including without limitation
# the rights to use, copy, modify, merge, publish, distribute, sublicense,
# and/or sell copies of the Software, and to permit persons to whom the
# Software is furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included
# in all copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL
# THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR
# OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE,
# ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR
# OTHER DEALINGS IN THE SOFTWARE.

# This SConstruct and the bdist tool are released under the MIT license;
# the pysdl2-cffi binding is GPL.

import sys
from distutils import sysconfig
import pytoml as toml
import enscons

metadata = dict(toml.load(open('pyproject.toml')))['tool']['enscons']

# most specific binary, non-manylinux1 tag should be at the top of this list
import wheel.pep425tags
for tag in wheel.pep425tags.get_supported():
    full_tag = '-'.join(tag)
    if not 'manylinux' in tag:
        break

env = Environment(tools=['default', 'packaging', enscons.generate],
                  PACKAGE_METADATA=metadata,
                  WHEEL_TAG=full_tag,
                  ROOT_IS_PURELIB=False)

env.Append(CPPPATH=[sysconfig.get_python_inc()])
env.Append(LIBPATH=[sysconfig.get_config_var('LIBDIR')])

PYTHON_LIBS = ['python' + sysconfig.get_config_var('VERSION')]

def get_build_command(name):
    return sys.executable + " -m builder.build_" + name

src_files = Glob('sdl/*.py') + Glob('_sdl*/*.py')

parts_targets = {'sdl': 'sdl/__init__.py',
                 'image': 'sdl/image.py',
                 'sdl_image': 'sdl/image.py',
                 'mixer': 'sdl/mixer.py',
                 'sdl_mixer': 'sdl/mixer.py',
                 'ttf': 'sdl/ttf.py',
                 'sdl_ttf': 'sdl/ttf.py',
                 }

gen_source = True
if gen_source:
    sdl = env.Command('sdl/__init__.py',
        Glob("builder/*.py") + Glob("_sdl/*.py") + Glob("_sdl/*.h"),
        get_build_command("sdl"))

    for part in ('image', 'mixer', 'ttf'):
        env.Command(parts_targets[part],
            sdl + Glob("builder/*.py") + Glob("_sdl_%s/*.py" % part) + Glob("_sdl_%s/*.h" % part),
            get_build_command(part))

from distutils import dist
from distutils.command.build_ext import build_ext
from _sdl.cdefs import _extension_args

modules = []

for part in ('sdl', 'sdl_image', 'sdl_mixer', 'sdl_ttf'):
    env.Command('__%s.c' % part,
        parts_targets[part],
        sys.executable + " -c \"import _%s.cdefs; _%s.cdefs.ffi.emit_c_code('$TARGET')\"" % (part, part))

    ext = build_ext(dist.Distribution(dict(name='__%s' % part)))

    FRAMEWORKS = []
    LIBS = PYTHON_LIBS
    if sys.platform == 'darwin':
        FRAMEWORKS = Split("SDL2 SDL2_image SDL2_mixer SDL2_ttf") # OSX
    else:
        LIBS += _extension_args(part.rsplit('_')[-1])['libraries']

    modules.append(env.LoadableModule(
            ext.get_ext_filename('__%s' % part),
            ['__%s.c' % part],
            LIBPREFIX = '',
            FRAMEWORKS = FRAMEWORKS,
            LIBS = LIBS
            ))

package = env.Package(
        NAME=env['PACKAGE_NAME'],
        VERSION=env['PACKAGE_METADATA']['version'],
        PACKAGETYPE='src_zip',
        source=FindSourceFiles() + ['PKG-INFO'],
        target=['dist/' + env['PACKAGE_NAME'] + '-' + env['PACKAGE_VERSION']],
        )

for module in modules:
    env.Whl('platlib', module)

py_source = Glob('_sdl*/*.py') + Glob('sdl/*.py')
env.Whl('platlib', py_source)
