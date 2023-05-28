# -*- coding: utf-8 -*-

"""
    @project: PyQt5Book
    @Author：董超
    @file：qt102_PrintApi.py
    @date：2023/5/27
    @software：PyCharm
    @github: https://github.com/dongchao612/PyQt5Book
"""

import sys
from PyQt5.QtWidgets import QWidget

if __name__ == '__main__':
    out = sys.stdout
    sys.stdout = open(r'QWidget.txt', 'w')
    help(QWidget)
    sys.stdout.close()
    sys.stdout = out
