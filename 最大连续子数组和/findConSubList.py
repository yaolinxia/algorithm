"""
解法一：蛮力法
1.从第一个数开始遍历，不断求累加的和，当和增加的时候，继续执行，否则停止
2.从第二个数再开始，和之前求出的和进行比较，如果和比之前的要大，则替换为新的和值
3.时间复杂度O(n^3),需要三个循环
"""

def findSub1(l):
    length = len(l)
    maxSum = 0
    currSum = 0
    for i in range(0, length):
        for j in range(i, length):
            for k in range(i, j+1):
                currSum += l[k]
            if currSum > maxSum:
                maxSum = currSum
            currSum = 0
    print(maxSum)

"""
解法二：
核心：
currSum = max(a[j], currSum + a[j])
maxSum = max(maxSum, currSum)
"""
def findSub2(l):
    currSum = 0
    maxSum = l[0]
    length = len(l)
    for i in range(0, length):
        currSum = max(l[i], currSum + l[i])
        maxSum = max(maxSum, currSum)
    print(maxSum)

if __name__ == "__main__":
    l = [1, -2, 3, 10, -4, 7, 2]
    findSub1(l)
    findSub2(l)
