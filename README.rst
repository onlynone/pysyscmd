===============================
System Commands
===============================

.. image:: https://img.shields.io/pypi/v/pysyscmd.svg
        :target: https://pypi.python.org/pypi/pysyscmd


Utility to call any system command from python. Examples::

  >>> from syscmd import *
  >>> from syscmd.cmds import git
  >>> res = git('ls-files')
  .editorconfig
  .gitignore
  AUTHORS.rst
  CONTRIBUTING.rst
  HISTORY.rst
  LICENSE
  MANIFEST.in
  README.rst
  docs/Makefile
  docs/authors.rst
  docs/conf.py
  docs/contributing.rst
  docs/history.rst
  docs/index.rst
  docs/installation.rst
  docs/make.bat
  docs/readme.rst
  docs/usage.rst
  requirements.txt
  setup.cfg
  setup.py
  syscmd/__init__.py
  syscmd/cmds.py
  tox.ini
  >>> print res
  0
  >>> res = git('ls-files', f=CHECK_OUTPUT)
  >>> print res
  .editorconfig
  .gitignore
  AUTHORS.rst
  CONTRIBUTING.rst
  HISTORY.rst
  LICENSE
  MANIFEST.in
  README.rst
  docs/Makefile
  docs/authors.rst
  docs/conf.py
  docs/contributing.rst
  docs/history.rst
  docs/index.rst
  docs/installation.rst
  docs/make.bat
  docs/readme.rst
  docs/usage.rst
  requirements.txt
  setup.cfg
  setup.py
  syscmd/__init__.py
  syscmd/cmds.py
  tox.ini

  >>> res = git('blah', f=CHECK_OUTPUT)
  git: 'blah' is not a git command. See 'git --help'.

  Did you mean this?
          blame
  Traceback (most recent call last):
    File "<stdin>", line 1, in <module>
    File "syscmd/cmds.py", line 58, in _cmd
      return f(full_args, **full_kwargs)
    File "/usr/local/Cellar/python/2.7.9/Frameworks/Python.framework/Versions/2.7/lib/python2.7/subprocess.py", line 573, in check_output
      raise CalledProcessError(retcode, cmd, output=output)
  subprocess.CalledProcessError: Command '('/usr/local/bin/git', 'blah')' returned non-zero exit status 1

* Free software: BSD license
* Documentation: https://pysyscmd.readthedocs.org.

Features
--------

* TODO