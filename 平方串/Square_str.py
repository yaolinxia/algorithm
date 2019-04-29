#!/usr/bin/env python
# _*_ coding:utf-8 _*_
"""
题目描述
如果一个字符串S是由两个字符串T连接而成,即S = T + T,
我们就称S叫做平方串,例如"","aabaab","xxxx"都是平方串.
牛牛现在有一个字符串s,请你帮助牛牛从s中移除尽量少的字符,
让剩下的字符串是一个平方串。换句话说,就是找出s的最长子序列并且这个子序列构成一个平方串。
"""

# 把字符串存到字典中
# 网上思路：https://www.nowcoder.com/questionTerminal/b43fb39898f448e39adbcffde5ff0dfc

def find_squ(s):
    # 定义一个字典
    print(len(s))
    d = {}
    for c in s:
        if c in d:
            d[c] += 1
        else:
            d[c] = 1
    print(d)
    # 遍历
    sum0 = 0
    # for m in d:
    #     print(d[m])
    for i in d:
        # print(d[i])
        sum0 = sum0 + (d[i]//2) * 2
    print(sum0)


if __name__ == '__main__':
    # s = "frankfurt"
    s = input()
    find_squ(s)