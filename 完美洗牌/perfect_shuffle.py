#!/usr/bin/env python
# _*_ coding:utf-8 _*_

"""
input：输入一个数组列表[a1, a2, a3, a4, b1, b2, b3, b4]
output: 洗牌后的数组列表[a1, b1, a2, b2, a3, b3, a4, b4]
"""

# 思路1：从b1,开始往后，依次向前面进行插入
def shuffle1(l):
    mid = int(len(l) / 2)
    print(mid)
    t = 1
    for i in range(0, len(l)):
        if (i+mid) < len(l):
            l.insert(i+t, l[i+mid])
            t += 1
            del l[mid]
    print(l)


# 思路2：使用perfectshufle的方法
def shuffle2(l):
    mid = int(len(l) / 2)
    # b = l[4:len(l)]
    # print(b)
    b = []
    # print(mid)
    for i in range(0, len(l)):
        b[((i+1)*2) % (len(l)+1)-1] = l[i]
    print(l)
    for i in range(0, len(l)+1):
        l[i] = b[i]


if __name__ == '__main__':
    l = ['a1', 'a2', 'a3', 'a4', 'b1', 'b2', 'b3', 'b4']
    shuffle2(l)

