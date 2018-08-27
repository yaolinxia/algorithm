#!/usr/bin/env python
# _*_ coding:utf-8 _*_

"""
编写程序，在原字符串中把字符串尾部的m个字符移动到字符串的头部，
要求：长度为n的字符串操作时间复杂度为O(n)，空间复杂度为O(1)。 
例如，原字符串为”Ilovebaofeng”，m=7，输出结果为：”baofengIlove”。

"""

class Solution(object):
    def RotatingStr(self, str, m):
        length = len(str)
        lstr = list(str)
        print(lstr)
        #1.先把字符串进行分割,分成两块
        print("1==================================")
        lstr1 = lstr[0:length-m]
        print(lstr1)
        lstr2 = lstr[length-m:length]
        print(lstr2)
        #2.对其中每一个分割出来的字符串进行字符串逆转
        print("2==================================")
        lstr1.reverse()
        print(lstr1)
        lstr2.reverse()
        print(lstr2)
        #3.将逆向的两个字符串合并在一起，然后再逆转
        print(lstr1+lstr2)
        SumStr = lstr1+lstr2
        (SumStr).reverse()
        print(SumStr)
        ReSumStr = "".join(SumStr)
        return ReSumStr

if __name__ == "__main__":
    str = "Ilovebaofeng"
    m = 7
    print(Solution().RotatingStr(str, m))