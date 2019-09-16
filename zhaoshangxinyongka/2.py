#!/usr/bin/env python
# _*_ coding:utf-8 _*_

# str.replace("is", "was")
def qumo(s):
    nums = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    n = 0
    s_n = 0
    for c in s:
        if c == "?":
            s_n += 1
    # print(s_n)
    t = 1
    li = []
    if s_n == 2:
        for c in nums:
            s1 = s.replace("?", c, 1)
            # print(s)
            for k in nums:
                s2 = s1.replace("?", k, 2)
                # print(s2)
                if (int(s2))%13 == 5:
                    n += 1
    elif s_n == 3:
        for c in nums:
            s1 = s.replace("?", c, 1)
            # print(s)
            for k in nums:
                s2 = s1.replace("?", k, 2)
                for g in nums:
                    s3 = s2.replace("?", g, 3)
                    # print(s2)
                    if (int(s3)) % 13 == 5:
                        n += 1
    elif s_n == 5:
        for c in nums:
            s1 = s.replace("?", c, 1)
            # print(s)
            for k in nums:
                s2 = s1.replace("?", k, 2)
                for g in nums:
                    s3 = s2.replace("?", g, 3)
                    for k2 in nums:
                        s4 = s3.replace("?", k2, 4)
                        # print(s2)
                        if (int(s4)) % 13 == 5:
                            n += 1

    print(n%(10^9+7))
    # for j in range(1, s_n):
    #     s = s.replace("?", i, j)
    #     for i in nums:
    #         s = s.replace("?", i, j)
    #         if (int(s))%13 == 5:
    #             n += 1

    # print(s1)
    # for i in nums:
    #     for j in nums:
    #         s1 = s.replace("?", j)
    #         print(int(s1))
    #     # if (int(s1))%13 == 5:
    #     #     n += 1
    # print(n)

                # print(s1)
    # s_list = s.strip().split()
    # # s_rev_l = s_list[::-1]





import sys
if __name__ == '__main__':
    # l = [1, 2, 3, 4, 3, 3,1,1]
    # N = int(sys.stdin.readline().strip('\n'))
    line = sys.stdin.readline().strip()
    # print(8)
    # li = list(map(int, line.split()))
    # li = []
    # for i in range(N):
    #     s = int(sys.stdin.readline().strip('\n'))
    #     li.append(s)
    # s = "2??"
    # print(qumo(s))
    qumo(line)