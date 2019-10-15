
def xuanzhuan(nums):
    if len(nums) == 0 or len(nums[0]) == 0:
        return []
    temp = []
    left, top = 0, 0
    down, right = len(nums) - 1, len(nums[0]) - 1
    while left <= right and top <= down:
        for i in range(left, right + 1):
            temp += nums[top][i],
        top += 1
        for i in range(top, down + 1):
            temp += nums[i][right],
        right -= 1
        for i in reversed(range(left, right + 1)):
            temp += nums[down][i],
        down -= 1
        for i in reversed(range(top, down + 1)):
            temp += nums[i][left],
        left += 1
    return temp[:(len(nums) * len(nums[0]))]
"""
第一行：矩阵行数m，列数n，用空格隔开
其后m行：每一行的n个数字，用空格隔开
3 3
1 2 3 
4 5 6
7 8 9
"""

import sys
if __name__ == '__main__':
    nums = [[1, 2, 3, 5], [4, 5, 6, 9], [7, 8, 9,11]]
    # m = 3
    # n = 3
    line1 = sys.stdin.readline().strip()
    l = list(map(int, line1.split()))
    m = l[0] #行
    n = l[1] #列
    temp = []
    for i in range(m):
        lines = sys.stdin.readline().strip()
        # print(8)
        ls = list(map(int, lines.split()))
        temp.append(ls)

    print(str(xuanzhuan(temp))[1:-1])