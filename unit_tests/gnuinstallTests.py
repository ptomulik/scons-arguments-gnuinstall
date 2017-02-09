""" `gnuinstallTest`

Unit tests for gnuinstall
"""

__docformat__ = "restructuredText"

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

import gnuinstall
import unittest

# The mock module does not come as a part of python 2.x stdlib, it has to be
# installed separatelly. Here we detect whether mock is present and if not,
# we skip all the tests that use mock.
_mock_missing = True
try:
    # Try unittest.mock first (python 3.x) ...
    import unittest.mock as mock
    _mock_missing = False
except ImportError:
    try:
        # ... then try mock (python 2.x)
        import mock
        _mock_missing = False
    except ImportError:
        # mock not installed
        pass

_test_all_arguments = {
  'prefix' : {
      'help' : 'Installation prefix',
      'default' : '/usr/local',
      'metavar' : 'DIR'
  },
  'exec_prefix' : {
      'help' : 'Installation prefix for executable files',
      'default' : '${prefix}',
      'metavar' : 'DIR'
  },
  'bindir' : {
      'help' : 'The directory for installing executable programs that users can run.',
      'default' : '${exec_prefix}/bin',
      'metavar' : 'DIR'
  },
  'sbindir' : {
      'help' : 'The directory for installing executable programs that can be run from the'
             + ' shell, but are only generally useful to system administrators.',
      'default' : '${exec_prefix}/sbin',
      'metavar' : 'DIR'
  },
  'libexecdir' : {
      'help' : 'The directory for installing executable programs to be run by other'
             + ' programs rather than by users.',
      'default' : '${exec_prefix}/libexec',
      'metavar' : 'DIR'
  },
  'datarootdir' : {
      'help' : 'The root of the directory tree for read-only architecture-independent'
             + ' data files.',
      'default' : '${prefix}/share',
      'metavar' : 'DIR'
  },
  'datadir' : {
      'help' : 'The directory for installing idiosyncratic read-only'
             + ' architecture-independent data files for this program.',
      'default' : '${datarootdir}',
      'metavar' : 'DIR'
  },
  'sysconfdir' : {
      'help' : 'The directory for installing read-only data files that pertain to a single'
             + ' machine - that is to say, files for configuring a host.',
      'default' : '${prefix}/etc',
      'metavar' : 'DIR'
  },
  'sharedstatedir' : {
      'help' : 'The directory for installing architecture-independent data files which'
             + ' the programs modify while they run.',
      'default' : '${prefix}/com',
      'metavar' : 'DIR'
  },
  'localstatedir' : {
      'help' : 'The directory for installing data files which the programs modify while'
             + ' they run, and that pertain to one specific machine.',
      'default' : '${prefix}/var',
      'metavar' : 'DIR'
  },
  'includedir' : {
      'help' : 'The directory for installing header files to be included by user programs'
             + ' with the C "#include" preprocessor directive.',
      'default' : '${prefix}/include',
      'metavar' : 'DIR'
  },
  'oldincludedir' : {
      'help' : 'The directory for installing "#include" header files for use with compilers'
             + ' other than GCC.',
      'default' : '/usr/include',
      'metavar' : 'DIR'
  },
  'docdir' : {
      'help' : 'The directory for installing documentation files (other than Info) for this'
                + ' package.',
      'default' : '${datarootdir}/doc/${install_package}',
      'metavar' : 'DIR'
  },
  'infodir' : {
      'help' : 'The directory for installing the Info files for this package.',
      'default' : '${datarootdir}/info',
      'metavar' : 'DIR'
  },
  'htmldir' : {
      'help' : 'Directory for installing documentation files in the html format.',
      'default' : '${docdir}',
      'metavar' : 'DIR'
  },
  'dvidir' : {
      'help' : 'Directory for installing documentation files in the dvi format.',
      'default' : '${docdir}',
      'metavar' : 'DIR'
  },
  'pdfdir' : {
      'help' : 'Directory for installing documentation files in the pdf format.',
      'default' : '${docdir}',
      'metavar' : 'DIR'
  },
  'psdir' : {
      'help' : 'Directory for installing documentation files in the ps format.',
      'default' : '${docdir}',
      'metavar' : 'DIR'
  },
  'libdir' : {
      'help' : 'The directory for object files and libraries of object code.',
      'default' : '${exec_prefix}/lib',
      'metavar' : 'DIR'
  },
  'lispdir' : {
      'help' : 'The directory for installing any Emacs Lisp files in this package.',
      'default' : '${datarootdir}/emacs/site-lisp',
      'metavar' : 'DIR'
  },
  'localedir' : {
      'help' : 'The directory for installing locale-specific message catalogs for this'
             + ' package.',
      'default' : '${datarootdir}/locale',
      'metavar' : 'DIR'
  },
  'mandir' : {
      'help' : 'The top-level directory for installing the man pages (if any) for this'
             + ' package.',
      'default' : '${datarootdir}/man',
      'metavar' : 'DIR'
  },
  'pkgdatadir' : {
      'help' : 'The directory for installing idiosyncratic read-only'
             + ' architecture-independent data files for this program.',
      'default' : '${datadir}/${package}',
      'metavar' : 'DIR'
  },
  'pkgincludedir' : {
      'help' : 'The directory for installing header files to be included by user programs'
             + ' with the C "#include" preprocessor directive.',
      'default' : '${includedir}/${package}',
      'metavar' : 'DIR'
  },
  'pkglibdir' : {
      'help' : 'The directory for object files and libraries of object code.',
      'default' : '${libdir}/${package}',
      'metavar' : 'DIR'
  },
  'pkglibexecdir' : {
      'help' : 'The directory for installing executable programs to be run by other'
             + ' programs rather than by users.',
      'default' : '${libexecdir}/${package}',
      'metavar' : 'DIR'
  }
}

_test_groups = {
    'dirs' : [
        'prefix',
        'exec_prefix',
        'bindir',
        'sbindir',
        'libexecdir',
        'datarootdir',
        'datadir',
        'sysconfdir',
        'sharedstatedir',
        'localstatedir',
        'includedir',
        'oldincludedir',
        'docdir',
        'infodir',
        'htmldir',
        'dvidir',
        'pdfdir',
        'psdir',
        'libdir',
        'lispdir',
        'localedir',
        'mandir',
        'pkgdatadir',
        'pkgincludedir',
        'pkglibdir',
        'pkglibexecdir',
    ]
}

#############################################################################
def __init_module_vars(**kw):
    man_sections = kw.get('man_sections', map(lambda x : str(x), range(1,10)) + ['n','l'])
    for sec in man_sections:
        dir_help = 'The directory for installing section %s man pages.' % sec
        ext_help = 'The file name extension for installed section %s man pages.' % sec
        _test_all_arguments['man%sdir' % sec] = { 'help' : dir_help, 'default' : '${mandir}/man%s' %sec, 'metavar' : 'DIR' }
        _test_all_arguments['man%sext' % sec] = { 'help' : ext_help, 'default' : '.%s' %sec, 'metavar' : 'DIR' }
        _test_groups['dirs'].append('man%sdir' % sec)
        _test_groups['dirs'].append('man%sext' % sec)
__init_module_vars()

#############################################################################
class Test__all_arguments(unittest.TestCase):
    """Test _all_arguments"""
    def check_argument(self,name):
        t1 = gnuinstall._all_arguments[name]
        t2 = _test_all_arguments[name]
        self.assertEqual(t1, t2)

    def test_prefix(self):
        """Test 'prefix' in _all_arguments"""
        self.check_argument('prefix')
    def test_exec_prefix(self):
        """Test 'exec_prefix' in _all_arguments"""
        self.check_argument('exec_prefix')
    def test_bindir(self):
        """Test 'bindir' in _all_arguments"""
        self.check_argument('bindir')
    def test_sbindir(self):
        """Test 'sbindir' in _all_arguments"""
        self.check_argument('sbindir')
    def test_libexecdir(self):
        """Test 'libexecdir' in _all_arguments"""
        self.check_argument('libexecdir')
    def test_datarootdir(self):
        """Test 'datarootdir' in _all_arguments"""
        self.check_argument('datarootdir')
    def test_datadir(self):
        """Test 'XXX' in _all_arguments"""
        self.check_argument('datadir')
    def test_sysconfdir(self):
        """Test 'sysconfdir' in _all_arguments"""
        self.check_argument('sysconfdir')
    def test_sharedstatedir(self):
        """Test 'sharedstatedir' in _all_arguments"""
        self.check_argument('sharedstatedir')
    def test_localstatedir(self):
        """Test 'localstatedir' in _all_arguments"""
        self.check_argument('localstatedir')
    def test_includedir(self):
        """Test 'includedir' in _all_arguments"""
        self.check_argument('includedir')
    def test_oldincludedir(self):
        """Test 'oldincludedir' in _all_arguments"""
        self.check_argument('oldincludedir')
    def test_docdir(self):
        """Test 'docdir' in _all_arguments"""
        self.check_argument('docdir')
    def test_infodir(self):
        """Test 'infodir' in _all_arguments"""
        self.check_argument('infodir')
    def test_htmldir(self):
        """Test 'htmldir' in _all_arguments"""
        self.check_argument('htmldir')
    def test_dvidir(self):
        """Test 'dvidir' in _all_arguments"""
        self.check_argument('dvidir')
    def test_pdfdir(self):
        """Test 'pdfdir' in _all_arguments"""
        self.check_argument('pdfdir')
    def test_psdir(self):
        """Test 'psdir' in _all_arguments"""
        self.check_argument('psdir')
    def test_libdir(self):
        """Test 'libdir' in _all_arguments"""
        self.check_argument('libdir')
    def test_lispdir(self):
        """Test 'lispdir' in _all_arguments"""
        self.check_argument('lispdir')
    def test_localedir(self):
        """Test 'localedir' in _all_arguments"""
        self.check_argument('localedir')
    def test_mandir(self):
        """Test 'mandir' in _all_arguments"""
        self.check_argument('mandir')
    def test_man1dir(self):
        """Test 'man1dir' in _all_arguments"""
        self.check_argument('man1dir')
    def test_man2dir(self):
        """Test 'man2dir' in _all_arguments"""
        self.check_argument('man2dir')
    def test_man3dir(self):
        """Test 'man3dir' in _all_arguments"""
        self.check_argument('man3dir')
    def test_man4dir(self):
        """Test 'man4dir' in _all_arguments"""
        self.check_argument('man4dir')
    def test_man5dir(self):
        """Test 'man5dir' in _all_arguments"""
        self.check_argument('man5dir')
    def test_man6dir(self):
        """Test 'man6dir' in _all_arguments"""
        self.check_argument('man6dir')
    def test_man7dir(self):
        """Test 'man7dir' in _all_arguments"""
        self.check_argument('man7dir')
    def test_man8dir(self):
        """Test 'man8dir' in _all_arguments"""
        self.check_argument('man8dir')
    def test_man9dir(self):
        """Test 'man9dir' in _all_arguments"""
        self.check_argument('man9dir')
    def test_manndir(self):
        """Test 'manndir' in _all_arguments"""
        self.check_argument('manndir')
    def test_manldir(self):
        """Test 'manldir' in _all_arguments"""
        self.check_argument('manldir')
    def test_man1ext(self):
        """Test 'man1ext' in _all_arguments"""
        self.check_argument('man1ext')
    def test_man2ext(self):
        """Test 'man2ext' in _all_arguments"""
        self.check_argument('man2ext')
    def test_man3ext(self):
        """Test 'man3ext' in _all_arguments"""
        self.check_argument('man3ext')
    def test_man4ext(self):
        """Test 'man4ext' in _all_arguments"""
        self.check_argument('man4ext')
    def test_man5ext(self):
        """Test 'man5ext' in _all_arguments"""
        self.check_argument('man5ext')
    def test_man6ext(self):
        """Test 'man6ext' in _all_arguments"""
        self.check_argument('man6ext')
    def test_man7ext(self):
        """Test 'man7ext' in _all_arguments"""
        self.check_argument('man7ext')
    def test_man8ext(self):
        """Test 'man8ext' in _all_arguments"""
        self.check_argument('man8ext')
    def test_man9ext(self):
        """Test 'man9ext' in _all_arguments"""
        self.check_argument('man9ext')
    def test_mannext(self):
        """Test 'mannext' in _all_arguments"""
        self.check_argument('mannext')
    def test_manlext(self):
        """Test 'manlext' in _all_arguments"""
        self.check_argument('manlext')
    def test_pkgdatadir(self):
        """Test 'pkgdatadir' in _all_arguments"""
        self.check_argument('pkgdatadir')
    def test_pkgincludedir(self):
        """Test 'pkgincludedir' in _all_arguments"""
        self.check_argument('pkgincludedir')
    def test_pkglibdir(self):
        """Test 'pkglibdir' in _all_arguments"""
        self.check_argument('pkglibdir')
    def test_pkglibexecdir(self):
        """Test 'pkglibexecdir' in _all_arguments"""
        self.check_argument('pkglibexecdir')

class Test_arguments(unittest.TestCase):
    def test_arguments_1(self):
        """gnuinstall.arguments() should return all argument declaratins"""
        decls = gnuinstall.arguments()
        self.assertEqual(type(decls), dict)
        self.assertEqual(decls, _test_all_arguments)

    def test_arguments_2(self):
        """gnuinstall.arguments(include_groups = 'dirs') should only include arguments from the 'dirs' group"""
        decls = gnuinstall.arguments(include_groups = 'dirs')
        expected = { k : _test_all_arguments[k] for k in _test_groups['dirs']}
        self.assertEqual(type(decls), dict)
        self.assertEqual(decls, expected)

    def test_arguments_3(self):
        """gnuinstall.arguments(exclude_groups = 'dirs') should exclude arguments from the 'dirs' group"""
        decls = gnuinstall.arguments(exclude_groups = 'dirs')
        expected = { k : _test_all_arguments[k] for k in (set(_test_all_arguments.keys()) - set(_test_groups['dirs']))}
        self.assertEqual(type(decls), dict)
        self.assertEqual(decls, expected)

#############################################################################
if __name__ == "__main__":
    ldr = unittest.TestLoader()
    suite = unittest.TestSuite()
    # Load tests to test suite
    tclasses = [ Test__all_arguments
               , Test_arguments
               ]

    for tclass in tclasses:
        suite.addTests(ldr.loadTestsFromTestCase(tclass))

    if not unittest.TextTestRunner(verbosity = 2).run(suite).wasSuccessful():
        sys.exit(1)

# Local Variables:
# # tab-width:4
# # indent-tabs-mode:nil
# # End:
# vim: set syntax=python expandtab tabstop=4 shiftwidth=4:
