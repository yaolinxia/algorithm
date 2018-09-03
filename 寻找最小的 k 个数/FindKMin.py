
class Solution(object):
    #方法一，将最先遍历的k个数存入数组中，再对后面的进行相应的处理
    def FindKMin(self, l, k):
        length = len(l)
        #1，首先进行遍历，将数组存入大小为k的数组中
        temp = []
        for i in range(0, k):
            temp.append(l[i])
        print(temp)
        #2，找出其中的最大值kmax
        index = Solution().findMax(temp)
        kmax = l[index]
        print("kamx", kmax)
        print(index)
        print("=========================")
        #3, 继续遍历剩余的n-k个数，与kmax进行比较
        for j in range(k, length):
            #print(l[j])
            #kmax = temp[index]
            if l[j] < kmax:
                kmax = l[j]
                # print("kmax1", kmax)
                temp[index] = l[j]
                print(temp)
                index = Solution().findMax(temp)
                print(index)
            else:
                continue
        print(temp)

    def findMax(self, temp):
        kmax = max(temp)
        index = temp.index(kmax)
        #print(index)
        #print(kmax)
        return index

if __name__ == "__main__":
    l = [2, 1, 4, 5, 4, 3, 2, 1, 4, 0, 6, 5, 4, 9, 23]
    Solution().FindKMin(l, 4)
    print(Solution().findMax(l))