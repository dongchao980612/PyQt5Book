# -*- coding: utf-8 -*-

"""
    @project：PyQt5Book
    @Author：董超
    @file：py213property02.py
    @date：2023/5/28
    @software：PyCharm
    @github: https://github.com/dongchao612/PyQt5Book
"""


class MyClass(object):
    def __init__(self):
        self._param = None # _param（单“_”）完全可以看成是一个私有变量名，因为在模块与类外无法调用它

    @property  # 修饰方法，是方法可以像属性一样访问。
    def param(self):
        print("get param: %s" % self._param)
        return self._param

    @param.setter
    def param(self, value):
        print("set param: %s" % self._param)
        self._param = value

    @param.deleter
    def param(self):
        print("del param: %s" % self._param)
        del self._param


if __name__ == '__main__':
    cls = MyClass()
    cls.param = 10
    print("current param : %s " % cls.param)
    del cls.param
