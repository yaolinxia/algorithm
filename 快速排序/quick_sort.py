#!/usr/bin/env python
# _*_ coding:utf-8 _*_

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

def quick_sorted(n):
    pri = n[0]
    left = []
    right = []
    if len(n) == 1:
        return n
    for i in range(1, len(n)):
        if n[i] < pri:
            left.append(n[i])
        else:
            right.append(n[i])
    return quick_sorted(left) + [pri] + quick_sorted(right)

if __name__ == '__main__':
    n = [2, 1, 3, 4, 2]
    # print(quick_sort(n))
    print(quick_sorted(n))