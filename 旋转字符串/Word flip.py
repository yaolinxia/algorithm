#!/usr/bin/env python
# _*_ coding:utf-8 _*_
"""
单词翻转。输入一个英文句子，翻转句子中单词的顺序，
但单词内字符的顺序不变，
句子中单词以空格符隔开。为简单起见，标点符号和普通字母一样处理。
例如，输入“I am a student.”，则输出“student. a am I”。
"""
"""
思路：
1.以空格作为字符串分割
2.将字符串子部分，进行子部分字符串逆转
"""

class Solution(object):
    def WordFlip(self, string):
        s1 = string.split()
        s1.reverse()
        print(s1)

if __name__ == "__main__":
    s = "I am a student."
    Solution().WordFlip(s)


