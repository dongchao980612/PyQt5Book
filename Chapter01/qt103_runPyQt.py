# -*- coding: utf-8 -*-

"""
    @project: PyQt5Book
    @Author：董超
    @file：qt103_runPyQt.py
    @date：2023/5/27
    @software：PyCharm
    @github: https://github.com/dongchao612/PyQt5Book
"""

import sys
from PyQt5.QtWidgets import QApplication, QWidget

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = QWidget()
    window.resize(500, 500)
    window.move(300, 300)
    window.setWindowTitle('hello PyQt5')
    window.show()
    sys.exit(app.exec_())
