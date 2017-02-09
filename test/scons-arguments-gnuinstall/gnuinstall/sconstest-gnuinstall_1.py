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
Tests SConsArguments.ImportArguments('gnuinstall').
"""

import TestSCons

test = TestSCons.TestSCons()
test.file_fixture('../../../gnuinstall.py', 'site_scons/site_arguments/gnuinstall.py')
test.dir_fixture('../../../site_scons/SConsArguments', 'site_scons/SConsArguments')
test.write('SConstruct',
"""
# SConstruct
import SConsArguments

env = Environment()
var = Variables()
decls = SConsArguments.ImportArguments('gnuinstall')
args = decls.Commit(env, var, True)

AddOption('--help-variables', dest='help_variables', action='store_true',
          help='print help for CLI variables')
if GetOption('help_variables'):
    print args.GenerateVariablesHelpText(var, env)
""")

test.run('-Q --help-variables')

lines = [
"""docdir: The directory for installing documentation files (other than Info) for this package.""",
"""    default: ${datarootdir}/doc/${install_package}""",
"""    actual: /usr/local/share/doc/""",

"""sharedstatedir: The directory for installing architecture-independent data files which the programs modify while they run.""",
"""    default: ${prefix}/com""",
"""    actual: /usr/local/com""",

"""htmldir: Directory for installing documentation files in the html format.""",
"""    default: ${docdir}""",
"""    actual: /usr/local/share/doc/""",

"""localstatedir: The directory for installing data files which the programs modify while they run, and that pertain to one specific machine.""",
"""    default: ${prefix}/var""",
"""    actual: /usr/local/var""",

"""prefix: Installation prefix""",
"""    default: /usr/local""",
"""    actual: /usr/local""",

"""pkgdatadir: The directory for installing idiosyncratic read-only architecture-independent data files for this program.""",
"""    default: ${datadir}/${package}""",
"""    actual: /usr/local/share/""",

"""psdir: Directory for installing documentation files in the ps format.""",
"""    default: ${docdir}""",
"""    actual: /usr/local/share/doc/""",

"""mandir: The top-level directory for installing the man pages (if any) for this package.""",
"""    default: ${datarootdir}/man""",
"""    actual: /usr/local/share/man""",

"""infodir: The directory for installing the Info files for this package.""",
"""    default: ${datarootdir}/info""",
"""    actual: /usr/local/share/info""",

"""exec_prefix: Installation prefix for executable files""",
"""    default: ${prefix}""",
"""    actual: /usr/local""",

"""libdir: The directory for object files and libraries of object code.""",
"""    default: ${exec_prefix}/lib""",
"""    actual: /usr/local/lib""",

"""lispdir: The directory for installing any Emacs Lisp files in this package.""",
"""    default: ${datarootdir}/emacs/site-lisp""",
"""    actual: /usr/local/share/emacs/site-lisp""",

"""datadir: The directory for installing idiosyncratic read-only architecture-independent data files for this program.""",
"""    default: ${datarootdir}""",
"""    actual: /usr/local/share""",

"""pkglibdir: The directory for object files and libraries of object code.""",
"""    default: ${libdir}/${package}""",
"""    actual: /usr/local/lib/""",

"""dvidir: Directory for installing documentation files in the dvi format.""",
"""    default: ${docdir}""",
"""    actual: /usr/local/share/doc/""",

"""bindir: The directory for installing executable programs that users can run.""",
"""    default: ${exec_prefix}/bin""",
"""    actual: /usr/local/bin""",

"""localedir: The directory for installing locale-specific message catalogs for this package.""",
"""    default: ${datarootdir}/locale""",
"""    actual: /usr/local/share/locale""",

"""pkgincludedir: The directory for installing header files to be included by user programs with the C "#include" preprocessor directive.""",
"""    default: ${includedir}/${package}""",
"""    actual: /usr/local/include/""",

"""pdfdir: Directory for installing documentation files in the pdf format.""",
"""    default: ${docdir}""",
"""    actual: /usr/local/share/doc/""",

"""oldincludedir: The directory for installing "#include" header files for use with compilers other than GCC.""",
"""    default: /usr/include""",
"""    actual: /usr/include""",

"""datarootdir: The root of the directory tree for read-only architecture-independent data files.""",
"""    default: ${prefix}/share""",
"""    actual: /usr/local/share""",

"""pkglibexecdir: The directory for installing executable programs to be run by other programs rather than by users.""",
"""    default: ${libexecdir}/${package}""",
"""    actual: /usr/local/libexec/""",

"""sysconfdir: The directory for installing read-only data files that pertain to a single machine - that is to say, files for configuring a host.""",
"""    default: ${prefix}/etc""",
"""    actual: /usr/local/etc""",

"""includedir: The directory for installing header files to be included by user programs with the C "#include" preprocessor directive.""",
"""    default: ${prefix}/include""",
"""    actual: /usr/local/include""",

"""sbindir: The directory for installing executable programs that can be run from the shell, but are only generally useful to system administrators.""",
"""    default: ${exec_prefix}/sbin""",
"""    actual: /usr/local/sbin""",

"""libexecdir: The directory for installing executable programs to be run by other programs rather than by users.""",
"""    default: ${exec_prefix}/libexec""",
"""    actual: /usr/local/libexec""",

"""man1dir: The directory for installing section 1 man pages.""",
"""    default: ${mandir}/man1""",
"""    actual: /usr/local/share/man/man1""",

"""man1ext: The file name extension for installed section 1 man pages.""",
"""    default: .1""",
"""    actual: .1""",

"""man2dir: The directory for installing section 2 man pages.""",
"""    default: ${mandir}/man2""",
"""    actual: /usr/local/share/man/man2""",

"""man2ext: The file name extension for installed section 2 man pages.""",
"""    default: .2""",
"""    actual: .2""",

"""man3dir: The directory for installing section 3 man pages.""",
"""    default: ${mandir}/man3""",
"""    actual: /usr/local/share/man/man3""",

"""man3ext: The file name extension for installed section 3 man pages.""",
"""    default: .3""",
"""    actual: .3""",

"""man4dir: The directory for installing section 4 man pages.""",
"""    default: ${mandir}/man4""",
"""    actual: /usr/local/share/man/man4""",

"""man4ext: The file name extension for installed section 4 man pages.""",
"""    default: .4""",
"""    actual: .4""",

"""man5dir: The directory for installing section 5 man pages.""",
"""    default: ${mandir}/man5""",
"""    actual: /usr/local/share/man/man5""",

"""man5ext: The file name extension for installed section 5 man pages.""",
"""    default: .5""",
"""    actual: .5""",

"""man6dir: The directory for installing section 6 man pages.""",
"""    default: ${mandir}/man6""",
"""    actual: /usr/local/share/man/man6""",

"""man6ext: The file name extension for installed section 6 man pages.""",
"""    default: .6""",
"""    actual: .6""",

"""man7dir: The directory for installing section 7 man pages.""",
"""    default: ${mandir}/man7""",
"""    actual: /usr/local/share/man/man7""",

"""man7ext: The file name extension for installed section 7 man pages.""",
"""    default: .7""",
"""    actual: .7""",

"""man8dir: The directory for installing section 8 man pages.""",
"""    default: ${mandir}/man8""",
"""    actual: /usr/local/share/man/man8""",

"""man8ext: The file name extension for installed section 8 man pages.""",
"""    default: .8""",
"""    actual: .8""",

"""man9dir: The directory for installing section 9 man pages.""",
"""    default: ${mandir}/man9""",
"""    actual: /usr/local/share/man/man9""",

"""man9ext: The file name extension for installed section 9 man pages.""",
"""    default: .9""",
"""    actual: .9""",

"""manndir: The directory for installing section n man pages.""",
"""    default: ${mandir}/mann""",
"""    actual: /usr/local/share/man/mann""",

"""mannext: The file name extension for installed section n man pages.""",
"""    default: .n""",
"""    actual: .n""",

"""manldir: The directory for installing section l man pages.""",
"""    default: ${mandir}/manl""",
"""    actual: /usr/local/share/man/manl""",

"""manlext: The file name extension for installed section l man pages.""",
"""    default: .l""",
"""    actual: .l""",
]

test.must_contain_all_lines(test.stdout(), lines)

test.pass_test()

# Local Variables:
# # tab-width:4
# # indent-tabs-mode:nil
# # End:
# vim: set syntax=python expandtab tabstop=4 shiftwidth=4:
