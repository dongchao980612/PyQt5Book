# -*- coding: utf-8 -*-

"""
    @project: PyQt5Book
    @Author：董超
    @file：qt101_testPyQt.py
    @date：2023/5/27
    @software：PyCharm
    @github: https://github.com/dongchao612/PyQt5Book
"""

import sys
from PyQt5 import QtWidgets

if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    widget = QtWidgets.QWidget()
    widget.resize(360, 360)
    widget.setWindowTitle("hello, pyqt5")
    widget.show()
    sys.exit(app.exec_())