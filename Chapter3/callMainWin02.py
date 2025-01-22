#!/usr/bin/env python 
# -*- coding: utf-8 -*-
# Time    : 2025/1/22 21:03
# Author  : dongchao
# File    : callMainWin02.py
# Software: PyCharm


from PyQt5.QtWidgets import QApplication, QMainWindow

from Chapter3.MainWin02 import Ui_MainWindow


class MainMainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)

        self.setupUi(self)


if __name__ == "__main__":
    import sys

    app = QApplication(sys.argv)
    myMain = MainMainWindow()
    myMain.show()
    sys.exit(app.exec_())
