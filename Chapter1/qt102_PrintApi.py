#!/usr/bin/env python 
# -*- coding: utf-8 -*-
# Time    : 2025/1/22 19:58
# Author  : dongchao
# File    : qt102_PrintApi.py
# Software: PyCharm


import sys
from PyQt5.QtWidgets import QWidget

out = sys.stdout
sys.stdout = open("./QWidget.txt", "w")
help(QWidget)
sys.stdout.close()
sys.stdout = out
