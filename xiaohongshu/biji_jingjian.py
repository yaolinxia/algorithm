#!/usr/bin/env python
# _*_ coding:utf-8 _*_

# 挑选笔记，不能出现连续编号，需要点赞总数最多。两者都符合的时候，选择笔记总数最少的
# opt[i]表示前i篇文章获得的最多点赞数；arts[i]表示前总赞数最多时， 挑选的文章总数
def find_good(n, likes):
    opt = [0 for i in range(n)]
    arts = [0 for i in range(n)]
    opt[0], opt[1] = likes[0], likes[1]
    arts[0], arts[1] = 1, 1
    for i in range(2, n):
        num1 = opt[i-1]
        num2 = opt[i-2]
        if num1 >= num2:
            opt[i] = num1
            arts[i] = arts[i-1]
        else:
            opt[i] = num2
            arts[i] = arts[i-2] + 1
    return opt[-1], arts[-1]

import sys
if __name__ == '__main__':
    n = int(sys.stdin.readline().strip('\n'))
    likes = list(map(int, sys.stdin.readline().split(' ')))
    all, nums = find_good(n, likes)
    print("{0} {1}".format(all, nums))
