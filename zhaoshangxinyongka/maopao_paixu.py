#!/usr/bin/env python
# _*_ coding:utf-8 _*_

def maopao(l):
    num = 0
    for i in range(0, len(l)):
        for j in range(i+1, len(l)):
            if l[i] > l[j]:
                temp = l[i]
                l[i] = l[j]
                l[j] = temp
                num += 1
            else:
                continue
    # print(l)
    print(num)

def quick_sort(n):
    pivot = n[0]
    left = []
    right = []
    if len(n) == 1:
        return n
    for i in range(1, len(n)):
        if n[i] < pivot:
            left.append(n[i])
        else:
            right.append(n[i])

    return quick_sort(left) + [pivot] + quick_sort(right)
    # quick_sort(left)
    # quick_sort(right)

import sys
if __name__ == '__main__':
    l = [1, 2, 3, 4, 3, 3,1,1]
    N = int(sys.stdin.readline().strip('\n'))
    # line = sys.stdin.readline().strip()
    # li = list(map(int, line.split()))
    li = []
    for i in range(N):
        s = int(sys.stdin.readline().strip('\n'))
        li.append(s)
    maopao(li)