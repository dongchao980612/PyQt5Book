# -*- coding: utf-8 -*-

"""
    @project：PyQt5Book
    @Author：董超
    @file：py209fun.py
    @date：2023/5/28
    @software：PyCharm
    @github: https://github.com/dongchao612/PyQt5Book
"""

from functools import partial
# partial 用于创建一个偏函数，将默认参数包装一个可调用对象，返回结果也是可调用对象。


def add(a, b):
    return a + b


if __name__ == '__main__':
    # 1
    print('\n#1')
    rst1 = add(4, 2)
    print('add(4, 2)=', rst1)

    plus3 = partial(add, 3)
    plus5 = partial(add, 5)

    # 2
    print('\n#2')
    rst2 = plus3(4)
    print('plus3(4)=', rst2)

    rst3 = plus3(7)
    print('plus3(7)=', rst3)

    rst4 = plus5(10)
    print('plus5(10)=', rst4)
