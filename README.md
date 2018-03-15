test-flask-website
==================

A simple Flask website based on the [tutorial][flask/tutorial] for testing Travis CI with.


Developing on Windows
---------------------

To run `tox` on Windows, all target Python versions need to be installed and
available on the `%PATH%`. One simple way of doing this is with [Conda][conda].

### Conda

For our purposes [Miniconda][conda/mini] is perfect. It allows us to install
multiple Python versions in user space with ease. It is assumed there are no
other Python installations on the system.

Download the latest 64-bit Python 3 Miniconda installer for Windows. Install it
without altering the `PATH` during installation. Then add just
`C:\ProgramData\Miniconda3\Scripts` to the System `PATH`. Doing so allows easy
access to various Conda management programs but (deliberately) **does not** add
any Python interpreters to the `PATH`.

Create all the versions of Python needed in user space. These are installed to
`%LOCALAPPDATA%` unless manually specified otherwise.
```
> conda create --name py27 python=2.7
> conda create --name py35 python=3.5
> conda create --name py36 python=3.6
> conda env list
# conda environments:
#
base                  *  C:\ProgramData\Miniconda3
py27                     C:\Users\WayneB\AppData\Local\conda\conda\envs\py27
py35                     C:\Users\WayneB\AppData\Local\conda\conda\envs\py35
py36                     C:\Users\WayneB\AppData\Local\conda\conda\envs\py36
```

Now we can add the most recent version to the User `PATH` to serve as the
*default* version: `%LOCALAPPDATA%\conda\conda\envs\py36`.

```
> python --version
Python 3.6.4 :: Anaconda, Inc.
> activate py36
(py36) > python --version
Python 3.6.4 :: Anaconda, Inc.
```

To make the alternate versions of Python available to tox create a
`python2.7.cmd` script for each version on the `PATH` containing:
```cmd
@%~dp0..\py27\python.exe %*
```

Now we can start developing. Enable a development environment, then run the
following commands.

```
> git clone git@github.com:samuelharmer/test-flask-website.git
> cd test-flask-website
> set FLASK_APP=website
> set FLASK_DEBUG=true
> pip install --editable .
> flask initdb
> flask run
```


[conda]: https://conda.io
[conda/mini]: https://conda.io/miniconda.html
[flask/tutorial]: http://flask.pocoo.org/docs/0.12/tutorial/
