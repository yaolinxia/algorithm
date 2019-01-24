class Solution(object):
    """
    解法一    
    注意到取n，和不取n个区别即可，考虑是否取第n个数的策略，可以转化为一个只和前n-1个数相关的问题。    
    - 如果取第n个数，那么问题就转化为“取前n-1个数使得它们的和为sum-n”，对应的代码语句就是sumOfkNumber(sum - n, n - 1)；
    - 如果不取第n个数，那么问题就转化为“取前n-1个数使得他们的和为sum”，对应的代码语句为sumOfkNumber(sum, n - 1)。    
    """
    def ans1(self, Sum, n):
        l = []
        if Sum <= 0 or n <= 0:
            print(l)
            return
        if Sum == 0:
            print(n)
            for i in l:
                print("+", i)
            print('\n')
        l.insert(0, n)
        #包含有n的序列
        Solution().ans1(Sum-n, n-1)
        #不包含有n的序列
        del l[0]
        Solution().ans1(Sum, n-1)


"""
description：寻找和为定值的多个数
input：sum, 列表
output：输出对应的列表
date：2019/01/17
"""
"""
解法一
注意到取n，和不取n个区别即可，考虑是否取第n个数的策略，可以转化为一个只和前n-1个数相关的问题。
- 如果取第n个数，那么问题就转化为“取前n-1个数使得它们的和为sum-n”，对应的代码语句就是sumOfkNumber(sum - n, n - 1)；
- 如果不取第n个数，那么问题就转化为“取前n-1个数使得他们的和为sum”，对应的代码语句为sumOfkNumber(sum, n - 1)。
"""
# 蛮力法
def ans1(Sum, n):
    # 存放0-n的数组列表
    l = []
    for i in range(0, n + 1):
        l.append(i)
    for c in l:
        sub_l = []
        temp = Sum - c
        if temp in l:
            sub_l.append(c)
            sub_l.append(temp)
        if sub_l:
            print(sub_l)
    # temp = Sum - i
    # if temp in

if __name__ == "__main__":
    Sum = 10
    n = 10
    ans1(Sum, n)
