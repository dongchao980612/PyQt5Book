# -*- coding: utf-8 -*-

"""
    @project：PyQt5Book
    @Author：董超
    @file：py205tuple.py
    @date：2023/5/28
    @software：PyCharm
    @github: https://github.com/dongchao612/PyQt5Book
"""

if __name__ == '__main__':
    # 1
    print('\n#1')
    zlst = ('hello', 'PyQt5', '.', 'com')
    vlst = ('Top', 'Quant', '.', 'vip')
    print('zlst,', zlst)
    print('vlst,', vlst)

    # 2
    print('\n#2')
    s2 = zlst[1:]
    print('s2,', s2)
    s3 = zlst[1:3]
    print('s3,', s3)
    s4 = vlst[:3]
    print('s4,', s4)

    # 3
    print('\n#3')
    print('s2+s3,', s2 + s3)
    print('s3*2,', s3 * 2)
