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

__docformat__ = "restructuredText"

"""
Ensure that Example 1 from the user manual works.
"""

import TestSCons

test = TestSCons.TestSCons()
test.file_fixture('../../../__init__.py', 'site_scons/site_arguments/gnuinstall/__init__.py')
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

# The following add --help-variables option which documents CLI variables.
AddOption( '--help-variables', dest='help_variables', action='store_true',
         help='print help for CLI variables' )
if GetOption('help_variables'):
  print args.GenerateVariablesHelpText(var, env)
  Exit(0)

# The rest is quite usual
hello_i = env.InstallAs("${bindir}/hello", 'hello')   # NOTE the ${bindir}

env.Alias('install', hello_i)
env.AlwaysBuild('install')
""")

help_lines = [
"""docdir: The directory for installing documentation files (other than Info) for this package.""",
"""    default: ${datarootdir}/doc/${install_package}""",
"""    actual: /usr/local/share/doc/""",
"""prefix: Installation prefix""",
"""    default: /usr/local""",
"""    actual: /usr/local""",
"""prefix: Installation prefix""",
"""    default: /usr/local""",
"""    actual: /usr/local""",
"""bindir: The directory for installing executable programs that users can run.""",
"""    default: ${exec_prefix}/bin""",
"""    actual: /usr/local/bin""",
]
test.run(['-Q', '--help-variables'])
test.must_contain_all_lines(test.stdout(), help_lines)

test.pass_test()

# Local Variables:
# # tab-width:4
# # indent-tabs-mode:nil
# # End:
# vim: set syntax=python expandtab tabstop=4 shiftwidth=4:
