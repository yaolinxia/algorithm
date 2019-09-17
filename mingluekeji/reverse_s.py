#!/usr/bin/env python
# _*_ coding:utf-8 _*_


def reverse(s):
    s = s[:-1]
    s_list = s.strip().split()
    s_rev_l  = s_list[::-1]
    temp = ""
    for c in s_rev_l:
        temp = temp+ c +" "
    # print(s_rev_l)
    print(temp[:-1]+".")

def r(s):
    s_l = s.strip().split()
    s_l.reverse()
    print("".join(s_l))
    # print(s_l)

import sys
if __name__ == '__main__':
    # s = "I like beijing."
    s = sys.stdin.readline().strip('\n')
    reverse(s)
    # r(s)