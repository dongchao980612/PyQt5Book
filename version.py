#!/usr/bin/env python 
# -*- coding: utf-8 -*-
# Time    : 2025/1/22 19:34
# Author  : dongchao
# File    : version.py
# Software: PyCharm


import sys

from PyQt5.Qt import PYQT_VERSION_STR
from PyQt5.QtCore import QT_VERSION_STR

if __name__ == '__main__':
    print("Python 版本:", sys.version)
    print("Qt 版本:", QT_VERSION_STR)
    print("PyQt 版本:", PYQT_VERSION_STR)


