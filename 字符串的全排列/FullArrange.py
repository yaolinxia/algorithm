
class Solution(object):
    #1.递归实现https://blog.csdn.net/sty945/article/details/79839567
    #https://blog.csdn.net/qq_42015869/article/details/79996227，此博客写的很详细
    def FullArr1(self, lstr, begin, end):
        # lstr = list(string)
        # length = len(string)
        # if length <= 1:
        #     return string
        if begin >= end:
            print(lstr)
        else:
            j = begin
            for i in range(begin, end):
                #位置进行交换
                lstr[i], lstr[j] = lstr[j], lstr[i]
                Solution().FullArr1(lstr, begin+1, end)
                lstr[i], lstr[j] = lstr[j], lstr[i]

    #定义交换字符串位置
    def Swap(self, string, index):
        lstr = list(string)
        temp = lstr[index]
        lstr[index] = lstr[0]
        lstr[0] = temp
        return str(lstr)
    """
    case1:
    已知字符串里的字符是互不相同的，现在任意组合，比如ab，
    则输出aa，ab，ba，bb，编程按照字典序输出所有的组合。
    分析：非简单的全排列问题（跟全排列的形式不同,abc全排列的话，
    只有6个不同的输出）。 本题可用递归的思想，设置一个变量表示已输出的个数，
    然后当个数达到字符串长度时，就输出。
    """
    def case1(self, string, size, resPos):
        result = []
        if resPos == size:
            print(result)
        else:
            for i in range(0, size):
                result[resPos] = string[i]
                Solution().case1(result, string, size, resPos + 1)
        print(result)

    def case2(self, ls):
        pj = 0
        pk = 0
        maxK = []
        length = len(ls)
        for i in range(length-1, -1, -1):
            for j in range(length-2, -1, -1):
                #print(j)
                if ls[i] > ls[j]:
                    pj = ls[j]
                    print(pj)
                    for k in range(j+1, length):
                        if ls[k] > pj:
                            maxK.append(ls[k])
                    pk = max(maxK)
                else:
                    continue

if __name__ == "__main__":
    s = "ab"
    lstr = list(s)
    #print(Solution().FullArr1(lstr, 0, len(lstr)))
    #Solution().Swap(s, 1)
    #Solution().case1(s, 2, -1)
    # for i in range(0, 2):
    # print(i)
    l1 = [1, 2, 3]
    Solution().case2(l1)
