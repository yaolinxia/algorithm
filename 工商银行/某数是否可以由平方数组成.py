"""
输入一个整数N， 1<N<100,000,000, 判断是否可以由平方数相加构成,并且要求最后的平方数的个数越少越好；
eg:
输入：17
输出：1 16
"""

import math

def num_split(N):
    p = []
    t = 100000000
    for i in range(1, int(math.sqrt(t)+1)):
        p.append(i*i)
    if N in p:
        print(N)
    # print(p)
    # print(len(p))
    for i in range(1, len(p)):
        if N>p[i-1] and N<p[i]:
            N -= p[i-1]
            print(p[i-1])
            num_split(N)

if __name__ == '__main__':
    N = 19
    num_split(N)
