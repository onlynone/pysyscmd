===============================
System Commands
===============================

.. image:: https://img.shields.io/pypi/v/pysyscmd.svg
        :target: https://pypi.python.org/pypi/pysyscmd


Utility to call any system command from python.

Import any program that's on your PATH from ``syscmd.cmds`` and you'll get a
function that executes the program with the given positional arguments. By,
default, the function uses ``subprocess.check_call`` to execute the program. But
this can be changed by passing in one of ``syscmd.CALL``, ``syscmd.CHECK_CALL``,
``syscmd.CHECK_OUTPUT`` as the ``f`` argument to your function to get the
respective ``subprocess`` function. Expect the same behavior from the imported
``syscmd`` functions as the ``subprocess`` functions, eg. return value, standard
in/out/error, etc.

In addition to the positional arguments and ``f``, the imported functions also
accept all the keyword arguments of the underlying ``subprocess`` functions.

Examples::

  # Import various system commands
  >>> from syscmd.cmds import echo, ls, true, false

  # Run 'echo' with three positional arguments; stdout goes to stdout and the
  # exit code is returned
  >>> res = echo('one', 'two', 'three')
  one two three
  >>> print res
  0

  # Run 'ls' with no arguments
  >>> res = ls()
  #README.rst# CONTRIBUTING.rst LICENSE README.rst requirements.txt setup.py tox.ini
  AUTHORS.rst HISTORY.rst MANIFEST.in docs setup.cfg syscmd

  # Run 'ls' with the '-l' option on 'README.rst'
  >>> res = ls('-l', 'README.rst')
  -rw-r--r--  1 swillis  staff  1904 Apr 21 13:13 README.rst

  # Run 'true'
  >>> res = true()
  >>> print res
  0

  # Run 'false'
  >>> res = false()
  Traceback (most recent call last):
    File "<stdin>", line 1, in <module>
    File "syscmd/cmds.py", line 57, in _cmd
      return f(full_args, **full_kwargs)
    File "/usr/local/Cellar/python/2.7.9/Frameworks/Python.framework/Versions/2.7/lib/python2.7/subprocess.py", line 540, in check_call
      raise CalledProcessError(retcode, cmd)
  subprocess.CalledProcessError: Command '('/usr/bin/false',)' returned non-zero exit status 1

  # Uh-oh... non-zero exit code causes exception because its run with
  # 'subprocess.check_call'

  # Import CALL from syscmd
  >>> from syscmd import CALL
  >>> res = false(f=CALL)

  # Now running 'false' doesn't cause an exception, and it returns the exit code
  >>> print res
  1

* Free software: BSD license

Features
--------

* TODO
