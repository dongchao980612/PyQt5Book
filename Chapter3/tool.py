#!/usr/bin/env python 
# -*- coding: utf-8 -*-
# Time    : 2025/1/22 20:31
# Author  : dongchao
# File    : tool.py
# Software: PyCharm


import os
import os.path

# Ui 文件所在的路径
dir = "./"


# 列出目录下所有的UI文件
def listUiFiles():
    uiList = []
    files = os.listdir(dir)
    for filename in files:
        # print(dir+os.sep+filename)
        # print(filename)
        if os.path.splitext(filename)[1] == ".ui":
            uiList.append(filename)
    return uiList


# 把扩展名为.ui的文件改成扩展名为.py的文件
def transPyFile(filename):
    return os.path.splitext(filename)[0] + ".py"


def runMain():
    uiList = listUiFiles()
    for uiFile in uiList:
        pyfile = transPyFile(uiFile)
        cmd = "pyuic5 -o {pyfile} {uiFile}".format(pyfile=pyfile, uiFile=uiFile)
        # print(cmd)
        os.system(cmd)


if __name__ == '__main__':
    runMain()
