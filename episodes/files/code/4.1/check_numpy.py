"""Section 4.1: check that NumPy is installed in this project's environment.

Run this file after `python -m pip install numpy`.
If you see ModuleNotFoundError, NumPy is not installed in the virtual
environment that PyCharm is using for this project.
"""

import math      # standard library: comes with Python, nothing to install
import sys

import numpy     # third-party: must be installed with pip first

print("Square root from the standard library:", math.sqrt(49))
print("NumPy version:", numpy.__version__)
print("Python is running from:", sys.prefix)
