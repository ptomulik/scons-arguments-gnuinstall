#
# Copyright (c) 2012-2015 by Pawel Tomulik
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

__docformat__ = "restructuredText"

"""
Ensure that Example 1 from the user manual works.
"""

import TestSCons

test = TestSCons.TestSCons()
test.file_fixture('../../../gnuinstall.py', 'site_scons/site_arguments/gnuinstall.py')
test.dir_fixture('../../../site_scons/SConsArguments', 'site_scons/SConsArguments')
test.write('hello',
r"""
#! /bin/sh
echo 'hello world!'
""")
test.write('SConstruct',
r"""
# SConstruct
import SConsArguments

env = Environment()                                   # SCons environment, you should know it
var = Variables()                                     # container for SCons CLI variables

decls = SConsArguments.ImportArguments('gnuinstall')  # declare arguments
args  = decls.Commit(env, var, True)                  # say "no more arguments" to scons
args.Postprocess(env, var, True)                      # transfer CLI arguments to env

# The rest is quite usual
hello_i = env.InstallAs("${bindir}/hello", 'hello')   # NOTE the ${bindir}

env.Alias('install', hello_i)
env.AlwaysBuild('install')
""")

test.run(['-Q', 'install', 'prefix=preinst/usr'])
test.must_exist("hello")
test.must_exist(["preinst","usr","bin","hello"])

test.run(['-Q', '-c', 'install', 'prefix=preinst/usr'])
test.must_exist("hello")
test.must_not_exist(["preinst","usr","bin","hello"])

test.run(['-Q', 'install', 'exec_prefix=preinst/usr1'])
test.must_exist("hello")
test.must_exist(["preinst","usr1","bin","hello"])

test.pass_test()

# Local Variables:
# # tab-width:4
# # indent-tabs-mode:nil
# # End:
# vim: set syntax=python expandtab tabstop=4 shiftwidth=4:
