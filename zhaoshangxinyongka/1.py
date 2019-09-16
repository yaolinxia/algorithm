#!/usr/bin/env python
# _*_ coding:utf-8 _*_


import sys

def solution(s):
    # nums = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    # n = 0
    # s_n = 0
    # for c in s:
    #     if c == "?":
    #         s_n += 1
    # print(s_n)
    # t = 1
    # li = []
    # for j in range(1, s_n):
    #     s = s.replace("?", i, j)
    #     for i in nums:
    #         s = s.replace("?", i, j)
    #         if (int(s)) % 13 == 5:
    #             n += 1
    n = len(s)
    pp = [1] * n
    p = [1]*n
    cou = 0
    while True:
        cur = [0]* n
        cou += 1
        for i in range(n):
            if s[i] == 'L':
                cur[i-1] += p[i]
            else:
                cur[i+1] += p[i]
        if pp == cur:
            break
        else:
            pp = p
            p = cur

    if cou % 2 == 0:
        res = cur
    else:
        res = p
    return " ".join(list(map(str, res)))

s = sys.stdin.readline().strip()
print(solution(s))
