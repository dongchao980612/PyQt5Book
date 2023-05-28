# -*- coding: utf-8 -*-

"""
    @project：PyQt5Book
    @Author：董超
    @file：callMainWinSignalSlog01.py
    @date：2023/5/28
    @software：PyCharm
    @github: https://github.com/dongchao612/PyQt5Book
"""

import sys
from PyQt5.QtWidgets import QApplication, QMainWindow

from Chapter03.MainWinSignalSlog01.MainWinSignalSlog01 import Ui_Form


class MyMainWindow(QMainWindow, Ui_Form):
    def __init__(self, parent=None):
        super(MyMainWindow, self).__init__(parent)
        self.setupUi(self)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    myWin = MyMainWindow()
    myWin.show()
    sys.exit(app.exec_())
