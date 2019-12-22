#!/usr/bin/env python
# _*_ coding:utf-8 _*_

"""
在十进制表示中，任意一个正整数都可以用字符’0’-‘9’表示出来。但是当’0’-‘9’
这些字符每种字符的数量有限时，可能有些正整数就无法表示出来了。比如你有两个‘1’，
一个‘2’，那么你能表示出11，12，121等等，但是无法表示出10，122，200等数。 
现在你手上拥有一些字符，它们都是’0’-‘9’的字符。你可以选出其中一些字符然后
将它们组合成一个数字，那么你所无法组成的最小的正整数是多少？
"""
def minInt(num):
    num_list = list(str(num))
    # print(num_list.sort())
    num_list.sort()
    # print(num_list)
    # 初始化词典，value值为0
    d = {}
    for i in range(0, 10):
        d[i] = 0
    for e in num_list:
        d[int(e)] += 1
    l = []
    for j in range(0,10):
        if d[j] == 0:
            l.append(j)
    # print(l)
    if len(l) == 1:
        if l[0] == 0:
            print(10)
        else:
            print(l[0])
    else:
        if l[0] == 0:
            print(l[1])
        else:
            print(l[0])

if __name__ == '__main__':
    # num = 123456789
    num = int(input())
    minInt(num)
