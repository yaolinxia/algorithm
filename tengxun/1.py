#!/usr/bin/env python
# _*_ coding:utf-8 _*_

# dict 存放
def delete(n, li):
    d = {}
    for i in range(n):
        # print(li[i])
        if li[i] in d:
            d[li[i]] += 1
        else:
            d[li[i]] = 1
    # print(d)
    return d

import sys
import math
if __name__ == '__main__':
    n = 4
    li = [3, 3, 3,4]

    N = int(sys.stdin.readline().strip())
    for i in range(N):
        n = int(sys.stdin.readline().strip())
        line = sys.stdin.readline().strip()
        # 把每一行的数字分隔后转化成int列表
        li = list(map(int, line.split()))
        d = delete(n, li)
        # print(max(d.values()))
        if n/2 < max(d.values()):
            print("NO")
        else:
            print("YES")
    # for i in d.values():




# M = []
# for _ in range(N):
#     line = sys.stdin.readline().strip()
#     a = list(map(int, line.split()))
#     M.append(a)
# print(solution(M))
