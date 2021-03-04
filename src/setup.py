# The following simply exports sorter_gui.py as an executable for using the command:
# python setup.py py2exe

from distutils.core import setup
import py2exe

setup(console=['sorter_gui.py'])