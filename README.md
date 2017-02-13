scons-arguments-gnuinstall
==========================

| travis-ci | appveyor  | coveralls |
|-----------|-----------|-----------|
|[![Build Status](https://travis-ci.org/ptomulik/scons-arguments-gnuinstall.png?branch=master)](https://travis-ci.org/ptomulik/scons-arguments-gnuinstall)| [![Build status](https://ci.appveyor.com/api/projects/status/xdjcgb8tovt605ug?svg=true)](https://ci.appveyor.com/project/ptomulik/scons-arguments-gnuinstall) | [![Coverage Status](https://coveralls.io/repos/ptomulik/scons-arguments-gnuinstall/badge.svg?branch=master&service=github)](https://coveralls.io/github/ptomulik/scons-arguments-gnuinstall?branch=master) |

Welcome to ``scons-arguments-gnuinstall``.

The scons-arguments-gnuinstall package is an extension to SCons which provides
several predefined command-line variables that may be used when installing
files into standard GNU directories (installing GNU-like software). It's
possible to add the whole amount of standard GNU command line options/variables
to SCons may be done with just few lines of code.

**NOTE**: you'll also need [scons-arguments](https://github.com/ptomulik/scons-arguments)

INSTALLATION
------------

Copy ``gnuinstall.py`` to your ``site_scons/site_arguments/`` directory

    cp scons-arguments-gnuinstall/gnuinstall.py your/projects/site_scons/site_arguments

QUICK EXAMPLE
-------------

Installing shell script, named ``hello`` into ``$bindir``.

the ``hello`` script:

```bash
#! /bin/sh
echo 'hello world!'
```

and ``SConstruct`` file

```python
from SConsArguments import ImportArguments

env = Environment()                         # SCons environment, you should know it
var = Variables()                           # container for SCons CLI variables

decls = ImportArguments('gnuinstall')       # declare arguments
args  = decls.Commit(env, var, True)        # say "no more arguments" to scons
args.Postprocess(env, var, True)            # transfer CLI arguments to env

if args.HandleVariablesHelp(var, env):
  Exit(0)

# The rest is quite usual
hello_i = env.InstallAs("${bindir}/hello", 'hello')   # NOTE the ${bindir}

env.Alias('install', hello_i)
env.AlwaysBuild('install')
```

Installing:

```console
ptomulik@barakus:# scons -Q install prefix=preinst/usr
Install file: "hello" as "preinst/usr/bin/hello"
```

You may also type

```console
scons --help-variables
```

to see full list of command-line variables available.

DOCUMENTATION
-------------

### User documentation

Online User Manual may be found at:

  * <http://ptomulik.github.io/scons-arguments-gnuinstall/user/manual.html>

User documentation can be generated from the top level directory with the
following command (see also requirements below)

```shell
scons user-doc
```
The generated documentation is located in ``build/doc/user``.

### API documentation

Online API documentation may be found at:

  * <http://ptomulik.github.io/scons-arguments-gnuinstall/api/>

API documentation can be generated from the top level directory with the
following command (see also requirements below)

```shell
scons api-doc
```

The generated documentation will be written to ``build/doc/api``.

#### Requirements for user-doc

To generate user's documentation, you'll need following packages on your
system:

  * docbook5-xml <http://www.oasis-open.org/docbook/xml/>
  * xsltproc <ftp://xmlsoft.org/libxslt/>
  * imagemagick <http://www.imagemagick.org/>

You also must install locally the SCons docbook tool by Dirk Baechle:

  * scons docbook tool <https://bitbucket.org/dirkbaechle/scons_docbook/>

this is easily done by running the following bash script

```
python bin/downloads.py scons-docbook
```

or simply (to download all dependencies)

```
python bin/downloads.py
```

from the top level directory.

#### Requirements for api-doc

To generate API documentation, you may need following packages on your system:

  * python-epydoc <http://epydoc.sourceforge.net/>
  * python-docutils <http://pypi.python.org/pypi/docutils>
  * python-pygments <http://pygments.org/>

Note, that epydoc is no longer developed, last activities in the project are
dated to 2008. The pip epydoc package 3.0.1 is not usable with current versions
of python. Fortunately Debian package is patched to work with current python.
Please use the ``python-epydoc`` package installed with apt-get.

```shell
apt-get install python-epydoc python-docutils python-pygments
```

TESTING
-------

We provide unit tests and end-to-end tests.

### Requirements for tests

  * scons-arguments <https://github.com/ptomulik/scons-arguments>

Download and install it locally with

```shell
python ./bin/downloads.py scons-arguments
```

or just

```shell
python ./bin/downloads.py
```

### Running unit tests

To run unit tests type

```shell
scons unit-test
```

### Requirements for unit tests

  * python-unittest2 <https://pypi.python.org/pypi/unittest2>
  * python-mock <https://pypi.python.org/pypi/mock>

On Debian install them with:

```shell
apt-get install python-unittest2 python-mock
```

### Running end-to-end tests

To run end-to-end tests, type

```shell
scons test
```

End-to-end tests are stored under ``test/`` directory. To run particular test
type (on Linux):

```shell
SCONS_EXTERNAL_TEST=1 python runtest.py test/SConsGnuArguments/UserManual/sconstest-usermanual-example_1.py
```


### Requirements for end-to-end tests

  * SCons testing framework

Download the SCons testing framework with:

```shell
python ./bin/downloads.py scons-test
```

or

```shell
python ./bin/downloads.py
```

LICENSE
-------

Copyright (c) 2017 by Pawel Tomulik

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE
