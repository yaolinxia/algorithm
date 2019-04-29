#!/usr/bin/env python
# _*_ coding:utf-8 _*_

def find_uglyData(num):
    # m 存放2， 3， 5
    m = [2, 3, 5]
    i = 0
    count = 0
    while i < 3:
        if num % m[i] == 0:
            num = num / num



if __name__ == '__main__':
    num = 14
    # find_uglyData(num)
    print(sorted([2 ** i * 3 ** j * 5 ** k for i in range(30) for j in range(20) for k in range(15)])[int(input()) - 1])