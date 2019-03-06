#!/usr/bin/env python
# _*_ coding:utf-8 _*_
# 荷兰国旗
# date: 2019/02/17

"""
input: 国旗颜色的乱序排列,输入一个数组 0:代表红球，1：白球， 2：篮球
output: 颜色排序为红黄蓝，依次排序
"""

# 方法一：蛮力法，类似冒泡排序， 当成是一个排序问题来做，只不过其中的数只有0,1,2
def dutch_flag1(flags):
    for i in range(0, len(flags)):
        for j in range(i+1, len(flags)):
            if flags[i] > flags[j]:
                temp = flags[i]
                flags[i] = flags[j]
                flags[j] = temp
    print(flags)
    return flags

# 方法二：使用一种分治的思想，设置三个指针begin, current, end
# 思路：全部以current作为衡量标杆
def dutch_flag2(flags):
    begin = 0
    current = 1
    end = len(flags) - 1
    while current < end:
        if flags[current] == 0:
            temp = flags[current]
            flags[current] = flags[begin]
            flags[begin] = temp
            current += 1
            begin += 1
        if flags[current] == 1:
            current += 1
        if flags[current] == 2:
            temp = flags[current]
            flags[current] = flags[end]
            flags[end] = temp
            end -= 1
    print(flags)
    return flags

if __name__ == '__main__':
    flags = [1, 2, 0, 0, 0, 2, 1, 1, 0, 2, 2, 1, 0]
    flags2 = [1, 0, 2]
    dutch_flag2(flags2)


