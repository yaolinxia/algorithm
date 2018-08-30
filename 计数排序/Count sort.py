"""
计数排序
输入：一个待排序的数组
输出：排好序的数组
需要以空间换取时间
step1:遍历整个数组,从第一个数组开始依次寻找比其的小的元素的个数，然后并且记录下来
step2:采用CountNum记录相应元素比其小的元素的个数
step3:将cCountNum列表元素直接进行排序
"""

class Solution(object):
    def CountSort(self, s):

        #length记录列表中元素的个数
        length = len(s)
        print(s)
        CountNum = [0] * length
        print(CountNum)
        print(length)
        for i in range(0, length):
            temp = s[i]
            for j in range(i+1, length):
                if s[i]>s[j]:
                    CountNum[i] += 1
                if s[i]<=s[j]:
                    CountNum[j] += 1
            #print(s[i])
        print(CountNum)
        D = {}
        for k in range(0, length):
            D[CountNum[k]] = s[k]
        # D.keys(CountNum)
        # D.values(s)
        print(D.values())

if __name__ == "__main__":
    s = [62, 31, 84, 96, 19, 47]
    Solution().CountSort(s)