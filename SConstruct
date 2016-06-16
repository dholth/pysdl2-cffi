# 
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
import pytoml as toml

metadata = dict(toml.load(open('pyproject.toml')))['tool']['wheel']

# actually it should be the dictionary interface
env = Environment(tools=['default', 'packaging', 'bdist'], 
                  toolpath='.',
                  PACKAGE_METADATA=metadata)

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
    LIBS = []
    if sys.platform == 'darwin':
         FRAMEWORKS = Split("SDL2 SDL2_image SDL2_mixer SDL2_ttf") # OSX
    else:
        LIBS = _extension_args(part.rsplit('_')[-1])['libraries']

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
        source=FindSourceFiles() + ['PKG-INFO']
        )

def wheelmeta_builder(target, source, env):
    with open(target[0].get_path(), 'w') as f:
        f.write("""Wheel-Version: 1.0
Generator: SConstruct (0.0.1)
Root-Is-Purelib: false
Tag: cp27-none-linux_x86_64.whl
""")

env.Command('WHEEL', 'pyproject.toml', wheelmeta_builder)

env['WHEEL_PATH'] = 'build/wheel'
# avoid escaping problems with variable name followed by . :
env['WHEEL_DATA'] = '$WHEEL_PATH/$PACKAGE_NAME_SAFE-' + env['PACKAGE_VERSION'] + '.data'
env['DIST_INFO'] = '$WHEEL_PATH/$PACKAGE_NAME_SAFE-' + env['PACKAGE_VERSION'] + '.dist-info'

env.Command('$DIST_INFO/WHEEL', 'pyproject.toml', wheelmeta_builder)

env.InstallAs('$DIST_INFO/METADATA', 'METADATA')
# env.InstallAs('$DIST_INFO/WHEEL', 'WHEEL')

for module in modules:
    # assume there's only one file per module...
    env.InstallAs('$WHEEL_PATH/' + module[0].get_path(), [module])

py_source = Glob('_sdl*/*.py') + Glob('sdl/*.py')
py_dest = ['$WHEEL_PATH/' + s.get_path() for s in py_source]
env.InstallAs(py_dest, py_source)

whl = env.Zip(target = '$PACKAGE_NAME_SAFE-' + env['PACKAGE_VERSION'] + '-cp27-none-linux_x86_64.whl',
              source = 'build/wheel/', ZIPROOT='build/wheel/')

env.Clean(whl, env['WHEEL_PATH'])

import base64

def urlsafe_b64encode(data):
    """urlsafe_b64encode without padding"""
    return base64.urlsafe_b64encode(data).rstrip(b'=')

def add_manifest(target, source, env):
    """
    Add the wheel manifest.
    """
    # os.path.relpath
    import hashlib
    import zipfile
    archive = zipfile.ZipFile(target[0].get_path(), 'a')
    lines = []
    for f in archive.namelist():
        print("File: %s" % f)
        data = archive.read(f)
        size = len(data)
        digest = hashlib.sha256(data).digest()
        digest = "sha256="+(urlsafe_b64encode(digest).decode('ascii'))
        lines.append("%s,%s,%s" % (f.replace(',', ',,'), digest, size))

    record_path = '%s-%s.dist-info/RECORD' % (env['PACKAGE_NAME_SAFE'], env['PACKAGE_VERSION'])
    lines.append(record_path+',,')
    RECORD = '\n'.join(lines)
    archive.writestr(record_path, RECORD)

env.AddPostAction(whl, Action(add_manifest))
