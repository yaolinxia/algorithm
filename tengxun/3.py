#!/usr/bin/env python
# _*_ coding:utf-8 _*_

# dict 存放
def mat(n, p, q):
    # p(p)= C(n, p)*(1/2)^n
    fenzi = 1
    for i in range(1, n+1):
        fenzi = fenzi*i
    fenmu = 1
    for j in range(1, p+1):
        fenmu = fenmu*j
    fenmu2 = 1
    for t in range(1, q+1):
        fenmu2 = fenmu2*t
    C= fenzi / (fenmu*fenmu2)
    print((C*(1/2)**n)%100000007)



import sys
import math
if __name__ == '__main__':
    # mat(2,1,0)


    line = sys.stdin.readline().strip()
    # 把每一行的数字分隔后转化成int列表
    li = list(map(int, line.split()))
    mat(li[0], li[1], li[2])




# M = []
# for _ in range(N):
#     line = sys.stdin.readline().strip()
#     a = list(map(int, line.split()))
#     M.append(a)
# print(solution(M))
