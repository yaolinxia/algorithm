# 先排序
def find_max(d):
    # print(d)
    l_s = []
    for i in d:
        # print(i)
        l_s.append(i)
    l_s_s = sorted(l_s, reverse=True)
    # print(l_s_s)
    v0 = 0
    L = 0
    for a in l_s_s:
        L += v0*d[a]+0.5*a*(d[a]**2)
        v0 = v0 + a*d[a]
    print(L)

import sys
if __name__ == '__main__':
    # N = 2
    # d = {2: 1, 30: 2}
    N = int(input())
    # M = 2
    # l = [5, 2, 3, 4, 1, 6]
    d = {}
    for i in range(N):
        line1 = sys.stdin.readline().strip()
        l2 = list(map(int, line1.split()))
        # print(l2[0], l2[1])
        d[l2[0]] = l2[1]
    find_max(d)
