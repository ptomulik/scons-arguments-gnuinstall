#
# Copyright (c) 2017 by Pawel Tomulik
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in all
# copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE

import os
import sys
import shutil
import platform
import SCons.Errors

env = Environment( ENV = os.environ.copy() )
env.SetDefault(PACKAGE = 'gnuinstall')

VariantDir('build/doc', 'doc', duplicate = 0)
SConscript('build/doc/SConscript', exports = ['env'])

python = sys.executable

AddOption('--with-coverage', action='store_true', help='run unit-test via coverage')

if 'unit-test' in COMMAND_LINE_TARGETS:
    if not env.Dir('#site_scons/SConsArguments').exists():
        raise SCons.Errors.UserError('site_scons/SConsArguments not found, please run %(python)s bin/downloads.py' % locals())
    # Note: SCons modules are in sys.path
    env['ENV']['PYTHONPATH'] = os.pathsep.join(['build/preinst'] + sys.path)

def Symlink(target, source, env):
    os.symlink(target[0].dir.rel_path(source[0]), target[0].path)

if platform.system() == 'Windows':
    env.Append(BUILDERS = { 'Preinst' : Builder(action = Copy('$TARGET','$SOURCE')) } )
else:
    env.Append(BUILDERS = { 'Preinst' : Builder(action = Symlink) } )

preinsttargetdir = env.subst('build/preinst/$PACKAGE/')
preinstsources = [ '__init__.py' ]
for preinstsource in preinstsources:
    preinsttarget = '%s/%s' % (preinsttargetdir, preinstsource)
    env.Preinst(preinsttarget, preinstsource)

#unittestflags = "-v"
unittestflags = ""
if platform.system() == 'Windows':
    discoverflags = "-p *Tests.py"
else:
    discoverflags = "-p '*Tests.py'"
if GetOption('with_coverage'):
    coverageinclude='__init__.py'
    coverage = env.Detect('python-coverage') or env.Detect('coverage') or 'coverage'
    cmd = ' %(coverage)s run --include=%(coverageinclude)s' % locals()
else:
    cmd = python
unittestcom = '%(cmd)s -m unittest discover %(unittestflags)s %(discoverflags)s' % locals()

env.Ignore('build', 'build/preinst')
env.Clean('build', 'build/preinst')
env.Command('unit-test', 'build/preinst', unittestcom)
env.AlwaysBuild('unit-test')
env.Ignore('.', 'unit-test')

env.AlwaysBuild(env.Alias('test'))
if 'test' in COMMAND_LINE_TARGETS:
    if not env.File('#runtest.py').exists():
        raise SCons.Errors.UserError('runtest.py not found, please run %(python)s bin/downloads.py' % locals())
    if not env.Dir('#QMTest').exists():
        raise SCons.Errors.UserError('QMTest not found, please run %(python)s bin/downloads.py' % locals())
    if not env.Dir('#site_scons/SConsArguments').exists():
        raise SCons.Errors.UserError('site_scons/SConsArguments not found, please run %(python)s bin/downloads.py' % locals())
    testflags = "-a"
    testcom = '%(python)s runtest.py %(testflags)s' % locals()
    # Note: SCons modules are in sys.path
    env['ENV']['SCONS'] = sys.argv[0]
    env['ENV']['SCONS_EXTERNAL_TEST'] = '1'
    env.Execute(testcom, "Running end-to-end tests")

# Local Variables:
# # tab-width:4
# # indent-tabs-mode:nil
# # End:
# vim: set syntax=python expandtab tabstop=4 shiftwidth=4:
