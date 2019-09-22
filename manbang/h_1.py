#!/usr/bin/env python
# _*_ coding:utf-8 _*_

def find_diff(s):
    total = {}
    for c in s:
        if c in total:
            total[c] += 1
        else:
            total[c] = 1
    temp = ""
    for s_i in s:

        if s_i in total:
            temp += s_i
            del total[s_i]
    print(temp)


if __name__ == '__main__':
    s = "AMMMS@HKJ"
    find_diff(s)