"""
思路一：试试python自带的函数是否能够实现(可行)
思路二：网上参考解答，依次扫描字符串，不断乘以10加上当前字符串表示整数(可行)

"""
class Solution(object):
    def StrToInt1(self, string):
        print(int(string))

    def StrToInt2(self, string):
        Sum = int(string[0])
        for i in range(1, len(string)):
            Sum = Sum*10 + int(string[i])
            #print(Sum)
        print(Sum)

if __name__ == "__main__":
    s = "123"
    s1 = "2147483697111111111"
    Solution().StrToInt1(s)
    Solution().StrToInt2(s1)