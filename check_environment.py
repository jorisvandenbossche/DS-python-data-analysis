# This script is adapted from Andreas Mueller:
# https://github.com/amueller/scipy-2018-sklearn/blob/master/check_env.ipynb
# and glemaitre: https://github.com/glemaitre/pyparis-2018-sklearn/blob/master/check_environment.py

from __future__ import print_function
from distutils.version import LooseVersion as Version
import sys


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
        if Version(ver) < min_ver:
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
pyversion = Version(sys.version)
if pyversion >= "3":
    if pyversion < "3.6":
        print(FAIL, "Python version 3.6 is required,"
                    " but %s is installed." % sys.version)
else:
    print(FAIL, "Python 3 is required, but %s is installed." % sys.version)

print()
requirements = {'numpy': "1.9", 'matplotlib': "2.0",
                'pandas': "0.25", 'notebook': "5",
                'plotnine': '0.6',
                'pyproj': '1.9.5.1', 'requests': '2.18.0',
                'seaborn': '0.9.0', 'xlrd': '1.1.0'}

# now the dependencies
for lib, required_version in list(requirements.items()):
    import_version(lib, required_version)

# mplleaflet has no option to derive __version__
try:
    import mplleaflet
    print(OK, '%s can be loaded' % ('mplleaflet'))
except:
    print(FAIL, '%s can not be loaded.' % ('mplleaflet'))
