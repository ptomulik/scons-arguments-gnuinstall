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
Tests SConsArguments.ImportArguments('gnuinstall') - whether they enter
scons environment
"""

import TestSCons

test = TestSCons.TestSCons()
test.file_fixture('../../../gnuinstall.py', 'site_scons/site_arguments/gnuinstall.py')
test.dir_fixture('../../../site_scons/SConsArguments', 'site_scons/SConsArguments')
test.write('SConstruct',
"""
# SConstruct
import SConsArguments

env = Environment(tools = [])
env.Replace(install_package = 'my_install_package', package = 'my_package')
var = Variables()
decls = SConsArguments.ImportArguments('gnuinstall')
args = decls.Commit(env, var, True)
args.Postprocess(env, var, True)

proxy = args.EnvProxy(env)
for k in decls.keys():
    print proxy.subst("%s : ${%s}" % (k, k))
""")

test_tab = [
  (
    ['prefix=/my/prefix'],
    [
        """prefix : /my/prefix""",
        """exec_prefix : /my/prefix""",
        """bindir : /my/prefix/bin""",
        """sbindir : /my/prefix/sbin""",
        """libexecdir : /my/prefix/libexec""",
        """datarootdir : /my/prefix/share""",
        """datadir : /my/prefix/share""",
        """sysconfdir : /my/prefix/etc""",
        """localstatedir : /my/prefix/var""",
        """includedir : /my/prefix/include""",
        """oldincludedir : /usr/include""",
        """docdir : /my/prefix/share/doc/my_install_package""",
        """infodir : /my/prefix/share/info""",
        """htmldir : /my/prefix/share/doc/my_install_package""",
        """dvidir : /my/prefix/share/doc/my_install_package""",
        """pdfdir : /my/prefix/share/doc/my_install_package""",
        """psdir : /my/prefix/share/doc/my_install_package""",
        """libdir : /my/prefix/lib""",
        """lispdir : /my/prefix/share/emacs/site-lisp""",
        """localedir : /my/prefix/share/locale""",
        """mandir : /my/prefix/share/man""",
        """pkgdatadir : /my/prefix/share/my_package""",
        """pkgincludedir : /my/prefix/include/my_package""",
        """pkglibdir : /my/prefix/lib/my_package""",
        """pkglibexecdir : /my/prefix/libexec/my_package""",
        """man1dir : /my/prefix/share/man/man1""",
        """man2dir : /my/prefix/share/man/man2""",
        """man3dir : /my/prefix/share/man/man3""",
        """man4dir : /my/prefix/share/man/man4""",
        """man5dir : /my/prefix/share/man/man5""",
        """man6dir : /my/prefix/share/man/man6""",
        """man7dir : /my/prefix/share/man/man7""",
        """man8dir : /my/prefix/share/man/man8""",
        """manndir : /my/prefix/share/man/mann""",
        """manldir : /my/prefix/share/man/manl""",
    ]
  ),
  (
    ['prefix=/my/prefix', 'exec_prefix=/my/exec_prefix'],
    [
        """prefix : /my/prefix""",
        """exec_prefix : /my/exec_prefix""",
        """bindir : /my/exec_prefix/bin""",
        """sbindir : /my/exec_prefix/sbin""",
        """libexecdir : /my/exec_prefix/libexec""",
        """datarootdir : /my/prefix/share""",
        """datadir : /my/prefix/share""",
        """sysconfdir : /my/prefix/etc""",
        """localstatedir : /my/prefix/var""",
        """includedir : /my/prefix/include""",
        """oldincludedir : /usr/include""",
        """docdir : /my/prefix/share/doc/my_install_package""",
        """infodir : /my/prefix/share/info""",
        """htmldir : /my/prefix/share/doc/my_install_package""",
        """dvidir : /my/prefix/share/doc/my_install_package""",
        """pdfdir : /my/prefix/share/doc/my_install_package""",
        """psdir : /my/prefix/share/doc/my_install_package""",
        """libdir : /my/exec_prefix/lib""",
        """lispdir : /my/prefix/share/emacs/site-lisp""",
        """localedir : /my/prefix/share/locale""",
        """mandir : /my/prefix/share/man""",
        """pkgdatadir : /my/prefix/share/my_package""",
        """pkgincludedir : /my/prefix/include/my_package""",
        """pkglibdir : /my/exec_prefix/lib/my_package""",
        """pkglibexecdir : /my/exec_prefix/libexec/my_package""",
        """man1dir : /my/prefix/share/man/man1""",
        """man2dir : /my/prefix/share/man/man2""",
        """man3dir : /my/prefix/share/man/man3""",
        """man4dir : /my/prefix/share/man/man4""",
        """man5dir : /my/prefix/share/man/man5""",
        """man6dir : /my/prefix/share/man/man6""",
        """man7dir : /my/prefix/share/man/man7""",
        """man8dir : /my/prefix/share/man/man8""",
        """manndir : /my/prefix/share/man/mann""",
        """manldir : /my/prefix/share/man/manl""",
    ]
  ),
  (
    ['exec_prefix=/my/exec_prefix'],
    [
        """prefix : /usr/local""",
        """exec_prefix : /my/exec_prefix""",
        """bindir : /my/exec_prefix/bin""",
        """sbindir : /my/exec_prefix/sbin""",
        """libexecdir : /my/exec_prefix/libexec""",
        """datarootdir : /usr/local/share""",
        """datadir : /usr/local/share""",
        """sysconfdir : /usr/local/etc""",
        """localstatedir : /usr/local/var""",
        """includedir : /usr/local/include""",
        """oldincludedir : /usr/include""",
        """docdir : /usr/local/share/doc/my_install_package""",
        """infodir : /usr/local/share/info""",
        """htmldir : /usr/local/share/doc/my_install_package""",
        """dvidir : /usr/local/share/doc/my_install_package""",
        """pdfdir : /usr/local/share/doc/my_install_package""",
        """psdir : /usr/local/share/doc/my_install_package""",
        """libdir : /my/exec_prefix/lib""",
        """lispdir : /usr/local/share/emacs/site-lisp""",
        """localedir : /usr/local/share/locale""",
        """mandir : /usr/local/share/man""",
        """pkgdatadir : /usr/local/share/my_package""",
        """pkgincludedir : /usr/local/include/my_package""",
        """pkglibdir : /my/exec_prefix/lib/my_package""",
        """pkglibexecdir : /my/exec_prefix/libexec/my_package""",
        """man1dir : /usr/local/share/man/man1""",
        """man2dir : /usr/local/share/man/man2""",
        """man3dir : /usr/local/share/man/man3""",
        """man4dir : /usr/local/share/man/man4""",
        """man5dir : /usr/local/share/man/man5""",
        """man6dir : /usr/local/share/man/man6""",
        """man7dir : /usr/local/share/man/man7""",
        """man8dir : /usr/local/share/man/man8""",
        """manndir : /usr/local/share/man/mann""",
        """manldir : /usr/local/share/man/manl""",
    ]
  ),
  (
    [ "bindir=${exec_prefix}/mybin"],
    [
      """bindir : /usr/local/mybin""",
      """sbindir : /usr/local/sbin"""
    ]
  ),
  (
    [ "exec_prefix=/my/exec_prefix", "libexecdir=${exec_prefix}/mylibexec"],
    [
      """libexecdir : /my/exec_prefix/mylibexec""",
      """libdir : /my/exec_prefix/lib""",
      """pkglibexecdir : /my/exec_prefix/mylibexec/my_package""",
      """pkglibdir : /my/exec_prefix/lib/my_package""",
    ]
  ),
  (
    [ "exec_prefix=/my/exec_prefix", "libdir=${exec_prefix}/mylib"],
    [
      """libexecdir : /my/exec_prefix/libexec""",
      """libdir : /my/exec_prefix/mylib""",
      """pkglibexecdir : /my/exec_prefix/libexec/my_package""",
      """pkglibdir : /my/exec_prefix/mylib/my_package""",
    ]
  ),
  (
    [ "datarootdir=${prefix}/myshare" ],
    [
        """datarootdir : /usr/local/myshare""",
        """datadir : /usr/local/myshare""",
        """pkgdatadir : /usr/local/myshare/my_package""",
    ]
  ),
]

for cli_vars, chk_lines in test_tab:
    test.run(['-Q'] + cli_vars)
    test.must_contain_all_lines(test.stdout(), chk_lines)

test.pass_test()

# Local Variables:
# # tab-width:4
# # indent-tabs-mode:nil
# # End:
# vim: set syntax=python expandtab tabstop=4 shiftwidth=4:
