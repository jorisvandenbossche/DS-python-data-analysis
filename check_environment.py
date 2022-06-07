# This script is adapted from Andreas Mueller:
# https://github.com/amueller/scipy-2018-sklearn/blob/master/check_env.ipynb
# and glemaitre: https://github.com/glemaitre/pyparis-2018-sklearn/blob/master/check_environment.py

from __future__ import print_function
import sys

# packaging is not in the stdlib, but should be available as dependency of
# some other package (eg jupyterlab, matplotlib, ..)
from packaging import version

try:
    import curses
    curses.setupterm()
    assert curses.tigetnum("colors") > 2
    OK = "\x1b[1;%dm[ OK ]\x1b[0m" % (30 + curses.COLOR_GREEN)
    FAIL = "\x1b[1;%dm[FAIL]\x1b[0m" % (30 + curses.COLOR_RED)
except:
    OK = '[ OK ]'
    FAIL = '[FAIL]'

try:
    import importlib
except ImportError:
    print(FAIL, "Python version 3.4 is required,"
                " but %s is installed." % sys.version)


def import_version(pkg, min_ver, fail_msg=""):
    mod = None
    try:
        mod = importlib.import_module(pkg)
        if pkg in {'PIL'}:
            ver = mod.VERSION
        elif pkg in {'xlrd'}:
            ver = mod.__VERSION__
        else:
            ver = mod.__version__
        if version.parse(ver) < version.parse(min_ver):
            print(FAIL, "%s version %s or higher required, but %s installed."
                  % (lib, min_ver, ver))
        else:
            print(OK, '%s version %s' % (pkg, ver))
    except ImportError:
        print(FAIL, '%s not installed. %s' % (pkg, fail_msg))
    return mod


# first check the python version
print('Using python in', sys.prefix)
print(sys.version)
pyversion = version.parse(sys.version.split(" ")[0])
if pyversion >= version.parse("3"):
    if pyversion < version.parse("3.8"):
        print(FAIL, "Python version 3.8 is required,"
                    " but %s is installed." % sys.version)
else:
    print(FAIL, "Python 3 is required, but %s is installed." % sys.version)

print()
requirements = {'numpy': "1.9", 'matplotlib': "2.0",
                'pandas': "1.2", 'jupyterlab': "3",
                'pyproj': '2.6', 'requests': '2.18.0',
                'seaborn': '0.9.0'}

# now the dependencies
for lib, required_version in list(requirements.items()):
    import_version(lib, required_version)

# mplleaflet has no option to derive __version__
try:
    import mplleaflet
    print(OK, '%s can be loaded' % ('mplleaflet'))
except:
    print(FAIL, '%s can not be loaded.' % ('mplleaflet'))
