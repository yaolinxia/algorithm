#!/usr/bin/env python
# _*_ coding:utf-8 _*_

"""
description: 从 1~n 这 n 个整数中随机选取任意多个，输出所有可能的选择方案。
input:输入一个整数n， 从中随机取k个
output:输出每一种方案
"""
def expEnum(n, k):
    # 记录取数的值
    temp = 1
    # 先考虑取1个数的情况
    for i in range(1, n+1):
        print(i)
        if temp < k:
            for j in range(i+1, n+1):
                print(i, ";", j)


if __name__ == '__main__':
    n = 5
    k = 3
    expEnum(n, k)