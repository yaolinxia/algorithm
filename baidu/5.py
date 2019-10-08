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

def d(num, str_len, l):
    print(8)

def fun(strls):
    allres = []
    def twoPair(s1,s2):
        stack = []
        for k in range(len(s1)):
            newS1 = s2[:k+1] + s1[k+1:]
            newS2 = s1[:k+1] + s2[k+1:]
            if (newS1,newS2) not in allres:
                stack.append((newS1, newS2))
                allres.append((newS1, newS2))
        for v in stack:
            twoPair(v[0],v[1])
    for i in range(len(strls)):
        for j in range(i):
            twoPair(strls[i],strls[j])
    print(len(allres) % 100000000007)


import sys

if __name__ == '__main__':
    line = sys.stdin.readline().strip()
    # print(8)
    l = list(map(int, line.split()))
    num = l[0]
    str_len = l[1]
    l_t = []
    for i in range(num):
        l2 = sys.stdin.readline().strip()
        l_t.append(l2)
    # d(num, str_len, l_t)
    fun(l_t)