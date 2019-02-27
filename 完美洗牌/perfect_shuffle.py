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
    # step1: 设置一个额外的空间，存放[b1, b2, b3, b4]
    l_b = l[4:len(l)]
    # step2: 算出列表长度一半的大小
    mid = int(len(l)/2)
    print(mid)
    # step3: 再定义一个空列表，存放最终的结果
    l_last = ['0']*len(l)
    for i in range(1, mid+1):
        l_last[(2*i) % (2*mid+1) - 1] = l[i-1]
    for i in range(0, mid):
        l_last[(2*i)] = l_b[i]
    print(l_last)


if __name__ == '__main__':
    l = ['a1', 'a2', 'a3', 'a4', 'b1', 'b2', 'b3', 'b4']
    shuffle2(l)

