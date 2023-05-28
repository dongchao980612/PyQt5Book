# -*- coding: utf-8 -*-

"""
    @project：PyQt5Book
    @Author：董超
    @file：py211class.py
    @date：2023/5/28
    @software：PyCharm
    @github: https://github.com/dongchao612/PyQt5Book
"""


class MyClass:
    count = 0
    name = 'DefaultName'

    def __init__(self, name):
        self.name = name
        print('类的变量是%s\n对象的变量是:%s' % (MyClass.name, self.name))

    def setCount(self, count):
        self.count = count

    def getCount(self):
        return self.count


if __name__ == '__main__':
    cls = MyClass('lisi')
    cls.setCount(10)
    print('count=%d' % cls.getCount())
