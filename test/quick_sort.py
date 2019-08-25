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


def toutiao():
    # 本题为考试单行多行输入输出规范示例，无需提交，不计分。
    import sys
    for line in sys.stdin:
        a = line.split()
        print(int(a[0]) + int(a[1]))

def t2():
    # coding=utf-8
    # 本题为考试多行输入输出规范示例，无需提交，不计分。
    import sys
    if __name__ == "__main__":
        # 读取第一行的n
        n = int(sys.stdin.readline().strip())
        ans = 0
        for i in range(n):
            # 读取每一行
            line = sys.stdin.readline().strip()
            # 把每一行的数字分隔后转化成int列表
            values = list(map(int, line.split()))
            for v in values:
                ans += v
        print(ans)

def tangfeng():
    import sys
    # 2, 3, 5, 7两两比较，它们之间是否存在公约数
    # 先排序
    if __name__ == "__main__":
        # 读取第一行的n
        # num = 0
        #
        # n = int(sys.stdin.readline().strip())
        # for i in range(1):
        #     # 读取每一行
        #     line = sys.stdin.readline().strip()
        #     # 把每一行的数字分隔后转化成int列表
        #     values = list(map(int, line.split()))
        #     num_list = sorted(values)
        l = [20, 50, 22, 74, 9, 63]
        num_list = sorted(l)
        # print(num_list)
        yueshu = []
        dicc_y = {}
        for i in range(len(num_list)):
            yueshu_s = []
            for j in range(i+1, len(num_list)):
                print(num_list[i], num_list[j])
                x = hcf(num_list[i], num_list[j])
                if x > 1 and (x in dicc_y):
                    dicc_y[x] += 1
                if x > 1 and (x not in dicc_y):
                    dicc_y[x] = 1
            # yueshu.append(sorted(yueshu_s))
        print(max(dicc_y.values())-1)


# 定义一个函数 ，寻找两个数之间的公约数
def hcf(x, y):
    for i in range(1, x+1):
        if((x%i==0) and (y%i==0)):
            hcf = i
    return hcf

import sys
    # 2, 3, 5, 7两两比较，它们之间是否存在公约数
    # 先排序
if __name__ == "__main__":
    # 读取第一行的n
    # num = 0
    #
    # n = int(sys.stdin.readline().strip())
    # for i in range(1):
    #     # 读取每一行
    #     line = sys.stdin.readline().strip()
    #     # 把每一行的数字分隔后转化成int列表
    #     values = list(map(int, line.split()))
    #     num_list = sorted(values)
    l = [20, 50, 22, 74, 9, 63]
    num_list = sorted(l)
    # print(num_list)
    yueshu = []
    dicc_y = {}
    for i in range(len(num_list)):
        yueshu_s = []
        for j in range(i+1, len(num_list)):
            print(num_list[i], num_list[j])
            x = hcf(num_list[i], num_list[j])
            if x > 1 and (x in dicc_y):
                dicc_y[x] += 1
            if x > 1 and (x not in dicc_y):
                dicc_y[x] = 1
        # yueshu.append(sorted(yueshu_s))
    print(max(dicc_y.values())-1)


# 定义一个函数 ，寻找两个数之间的公约数
def hcf(x, y):
    for i in range(1, x+1):
        if((x%i==0) and (y%i==0)):
            hcf = i
    return hcf


if __name__ == '__main__':
    # n = [2, 1, 3, 4, 2]
    # print(quick_sort(n))
    # toutiao()
    tangfeng()