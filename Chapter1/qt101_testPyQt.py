#!/usr/bin/env python 
# -*- coding: utf-8 -*-
# Time    : 2025/1/22 19:50
# Author  : dongchao
# File    : qt101_testPyQt.py
# Software: PyCharm


import sys

from PyQt5 import QtWidgets, QtCore

if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    widget = QtWidgets.QWidget()
    widget.resize(360, 360)
    widget.setWindowTitle("Hello PyQt5")
    widget.show()
    sys.exit(app.exec_())
