# Usage: python setup.py py2exe
# exe will place at .\dist


from distutils.core import setup
import numpy
import py2exe

setup(console=['windows-user-side.py'])