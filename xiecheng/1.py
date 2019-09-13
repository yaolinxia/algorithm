#!/usr/bin/env python
# _*_ coding:utf-8 _*_
import sys
# dict 存放
def fenzu(s="aabcddc"):
    # print(list(s))
    d = {}
    for c in s:
        if c in d:
            d[c]+=1
        else:
            d[c]=1
    if len(d) == len(s):
        print(len(s))
        return len(s)
        # sys.stdout(len(s))
        # return len(s)
    zu = [1]*len(s)
    # zu_d = {}
    # print(zu)
    i = 0
    j = 1
    stat = 0
    while i < len(s) and j+1 < len(s):
        # while j+1 < len(s) and i < j:
        if s[i] == s[j]:
            zu[stat] += 1
            j += 1
            i += 1
        else:
            if s[j] == s[j+1]:
                i = j
                j = i+1
                stat = i
                zu[stat] += 1
            else:
                zu[stat] += 1
                i += 1
                j += 1
    l2 = []
    for c in zu:
        if c > 1:
            l2.append(c)
    # print(1)
    print(str(l2)[1:-1].strip())
    return str(l2)[1:-1].strip()
    # print(zu)


import math
# win 滑动窗口
if __name__ == '__main__':
    s = input()
    fenzu(s=s)
    # fenzu(s="aacbddc")
    # N = int(sys.stdin.readline().strip())
    # for i in range(N):
    #     n = int(sys.stdin.readline().strip())
    #     line = sys.stdin.readline().strip()
    #     # 把每一行的数字分隔后转化成int列表
    #     li = list(map(int, line.split()))
    #     # d = delete(n, li)
    #     # print(max(d.values()))
    #     if n/2 < max(d.values()):
    #         print("NO")
    #     else:
    #         print("YES")
    # for i in d.values():




# M = []
# for _ in range(N):
#     line = sys.stdin.readline().strip()
#     a = list(map(int, line.split()))
#     M.append(a)
# print(solution(M))
