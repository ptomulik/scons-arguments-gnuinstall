"""`gnuinstall`

Provides `GNU installation directories`_ as SCons *arguments*.

**General Description**

This module provides standard `GNU installation directories`_ defined by `GNU
Coding Standards`_, for example ``$prefix``, ``$bindir`` or ``$sysconfdir``.

**Quick start**

.. python::
    # SConstruct
    import SConsArguments

    env = Environment()
    var = Variables()
    decls = SConsArguments.ImportArguments('gnuinstall')
    args = decls.Commit(env, var, True)
    args.Postprocess(env, var, True)

    print env.subst("prefix : ${prefix}")
    print env.subst("bindir : ${bindir}")

Running examples::

    ptomulik@barakus:$ scons -Q
    prefix : /usr/local
    bindir : /usr/local/bin

    ptomulik@barakus:$ scons -Q prefix=/usr
    prefix : /usr
    bindir : /usr/bin


**Supported variables**

  prefix
      Installation prefix
  exec_prefix
      Installation prefix for executable files
  bindir
      The directory for installing executable programs that users can run.
  sbindir
      The directory for installing executable programs that can be run from the
      shell, but are only generally useful to system administrators.
  libexecdir
      The directory for installing executable programs to be run by other
      programs rather than by users.
  datarootdir
      The root of the directory tree for read-only architecture-independent
      data files.
  datadir
      The directory for installing idiosyncratic read-only
      architecture-independent data files for this program.
  sysconfdir
      The directory for installing read-only data files that pertain to a single
      machine - that is to say, files for configuring a host.
  sharedstatedir
      The directory for installing architecture-independent data files which
      the programs modify while they run.
  localstatedir
      The directory for installing data files which the programs modify while
      they run, and that pertain to one specific machine.
  includedir
      The directory for installing header files to be included by user programs
      with the C ``#include`` preprocessor directive.
  oldincludedir
      The directory for installing ``#include`` header files for use with compilers
      other than GCC.
  docdir
      The directory for installing documentation files (other than Info) for this
      package.
  infodir
      The directory for installing the Info files for this package.
  htmldir
      Directory for installing documentation files in the html format.
  dvidir
      Directory for installing documentation files in the dvi format.
  pdfdir
      Directory for installing documentation files in the pdf format.
  psdir
      Directory for installing documentation files in the ps format.
  libdir
      The directory for object files and libraries of object code.
  lispdir
      The directory for installing any Emacs Lisp files in this package.
  localedir
      The directory for installing locale-specific message catalogs for this
      package.
  mandir
      The top-level directory for installing the man pages (if any) for this
      package.
  man1dir .. man9dir
      Simmilar to mandir
  man1ext .. man9ext
      Extensions for manpage files.
  pkgdatadir
      The directory for installing idiosyncratic read-only
      architecture-independent data files for this program.
  pkgincludedir
      The directory for installing header files to be included by user programs
      with the C ``#include`` preprocessor directive.
  pkglibdir
      The directory for object files and libraries of object code.
  pkglibexecdir
      The directory for installing executable programs to be run by other
      programs rather than by users.

.. _GNU installation directories: http://www.gnu.org/prep/standards/html_node/Directory-Variables.html
.. _GNU Coding Standards: http://www.gnu.org/prep/standards/html_node/
"""


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

__docformat__ = 'restructuredText'

import os
from SConsArguments.Importer import export_arguments

_all_arguments = {
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
"""Standard list of arguments for GNU install directories. This is internal
attribute and IS **NOT a part of public API**"""

#############################################################################
_groups = {
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
    """Initializes some module-level variables. This is an internal function
    and IS **NOT a part of public API**."""
    man_sections = kw.get('man_sections', map(lambda x : str(x), range(1,10)) + ['n','l'])
    for sec in man_sections:
        dir_help = 'The directory for installing section %s man pages.' % sec
        ext_help = 'The file name extension for installed section %s man pages.' % sec
        _all_arguments['man%sdir' % sec] = { 'help' : dir_help, 'default' : '${mandir}/man%s' %sec, 'metavar' : 'DIR' }
        _all_arguments['man%sext' % sec] = { 'help' : ext_help, 'default' : '.%s' % sec, 'metavar' : 'DIR' }
        _groups['dirs'].append('man%sdir' % sec)
        _groups['dirs'].append('man%sext' % sec)
__init_module_vars()

###############################################################################
def arguments(**kw):
    """Returns argument declarations related to GNU-like file installation

    :Keywords:
        include_groups : str | list
            include only arguments assigned to these groups
        exclude_groups : str | list
            exclude arguments assigned to these groups
        gnuinstall_include_groups : str | list
            include only arguments assigned to these groups, this has higher
            priority than **include_groups**
        gnuinstall_exclude_groups : str | list
            exclude arguments assigned to these groups, this has higher
            priority than **exclude_groups**
    """
    return export_arguments('gnuinstall', _all_arguments, _groups, **kw)

# Local Variables:
# # tab-width:4
# # indent-tabs-mode:nil
# # End:
# vim: set syntax=python expandtab tabstop=4 shiftwidth=4:
