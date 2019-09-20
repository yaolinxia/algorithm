#!/bin/python3

import math
import os
import random
import re
import sys



#
# Complete the 'betterCompression' function below.
#
# The function is expected to return a STRING.
# The function accepts STRING s as parameter.
#

def betterCompression(s):
    # Write your code here
    num = {"1", "2", "3", "4", "5", "6", "7", "8", "9", "0"}
    d = {}
    # for i in range(len(s)):
    #     if s.isalpha(s[i]):
    #         for j in range(i+1,len(s))
    head = 0
    tail = 1
    while tail<len(s)-1:
        if s[head].isalpha():
            t = 0
            s_t =""
            while s[tail].isalnum():
                s_t = s_t + s[tail]
                t += 1
                tail += 1

            d[head] = int(s_t)
        head += t
    print(d)

from itertools import groupby
import re
def betterC(s):
    d = {}
    split_S = re.findall(r'[0-9]+|[a-z]+',s)
    i = 0
    while i < len(split_S)-1:
        if split_S[i] in d:
            d[split_S[i]] += int(split_S[i+1])
            i +=2
        else:
            d[split_S[i]] = int(split_S[i+1])
            i += 2
    # print(d)
    temp = ""
    # for h in split_S:
    #     if h in d:
    #         temp += h + str(d[h])
    #         del d[h]
    # print(temp)
    # d = sorted(d.keys())
    d2 = sorted(d.items(), key=lambda item:item[0])
    # print(d2)
    for k in d2:
        # print(k)
    # for c, k in zip(d, d.values()):
        temp = temp + str(k[0])+ str(k[1])
    print(temp)

    # print(split_S)


if __name__ == '__main__':
    # fptr = open(os.environ['OUTPUT_PATH'], 'w')

    # s = input()
    s = "a12c1a1b56"

    result = betterC(s)

    # fptr.write(result + '\n')
    #
    # fptr.close()
