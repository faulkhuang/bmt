# Usage: python setup.py py2exe
# exe will place at .\dist


from distutils.core import setup
from PIL import Image
from PIL import ImageGrab
import numpy
import py2exe

setup(option = {"py2exe":{"packages":["PIL"], "includes":["PIL.Image", "PIL.PngImagePlugin"]}},
      console=['windows-user-side.py'])