# -*- coding: utf-8 -*-

"""
    @project：PyQt5Book
    @Author：董超
    @file：py202str.py
    @date：2023/5/28
    @software：PyCharm
    @github: https://github.com/dongchao612/PyQt5Book
"""

if __name__ == '__main__':
    dss = 'hello pyqt5'
    print('dss', dss)

    # 1
    print('\n#1')
    s2 = dss[1:]
    print('s2,', s2)
    s3 = dss[1:3]
    print('s3,', s3)
    s4 = dss[:3]
    print('s4,', s4)

    # 2
    print('\n#2')
    s2 = dss[-1]
    print('s2,', s2)
    s3 = dss[1:-2]
    print('s3,', s3)
    dn = len(dss)
    print('dn,', dn)

    # 3
    print('\n#3')
    print('s2+s3,', s2 + s3)
    print('s3*2,', s3 * 2)
