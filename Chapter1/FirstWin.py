#!/usr/bin/env python 
# -*- coding: utf-8 -*-
# Time    : 2025/1/22 20:04
# Author  : dongchao
# File    : FirstWin.py
# Software: PyCharm


import  sys
from PyQt5.QtWidgets import QPushButton,QApplication,QWidget
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton

class WinForm(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)

        self.setGeometry(300, 300, 350, 350)  # 设置窗口位置和大小
        self.setWindowTitle("点击按钮关闭窗口")  # 设置窗口标题

        # 创建按钮
        quit_button = QPushButton("close", self)  # 修改变量名，避免与内置函数冲突
        quit_button.setGeometry(10, 10, 60, 35)  # 设置按钮位置和大小
        quit_button.setStyleSheet("background-color:red")  # 修改样式表中的拼写错误
        quit_button.clicked.connect(self.close)  # 点击按钮时关闭窗口

# 主程序入口
if __name__ == "__main__":
    import sys
    app = QApplication(sys.argv)  # 创建应用程序对象
    form = WinForm()  # 创建窗口实例
    form.show()  # 显示窗口
    sys.exit(app.exec_())  # 启动应用程序事件循环
