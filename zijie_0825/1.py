#!/usr/bin/env python
# _*_ coding:utf-8 _*_

def solution(M):
    p = list(range(len(M)))
    def f(x):
        if p[x]!=x:
            p[x] = f(p[x])
        return p[x]
    res = len(M)
    for row in range(len(M)):
        for col in range(len(M[0])):
            if row!=col and M[row][col] >= 3:
                px, py = f(row), f(col)
                if px != py:
                    p[py] = px
                    res -= 1
    return res

import sys

N = int(sys.stdin.readline().strip())
M = []
for _ in range(N):
    line = sys.stdin.readline().strip()
    a = list(map(int, line.split()))
    M.append(a)
print(solution(M))
