# __init__.py

__author__ = "Marc Abu El Ghait, Franck Bonneau and Vincent Esposito"
__copyright__ = "Copyright 2016-2022, Cisco"

__version__ = "0.9.7.6"
__status__ = "Development"

# https://realpython.com/pypi-publish-python-package/

# Workaround for Intersight SDK 1.0.9-2110 that contains a RecursionError
import sys
sys.setrecursionlimit(1500)
