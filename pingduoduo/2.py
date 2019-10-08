# 先排序
def find_min(N, M, l):
    t = 0
    temp = []
    for l_S in l:
        if l_S[0] in temp:
            t += l_S[1] - l_S[0]
        else:
            t += l_S[1] - l_S[0] + 1
            temp.append(l_S[0])
            # temp.append(l_S[1])
        print(t)

import sys
if __name__ == '__main__':
    # N = 4
    # M = 2
    # l1 = [1, 2]

    line1 = sys.stdin.readline().strip()
    l2 = list(map(int, line1.split()))
    N = l2[0]
    M = l2[1]
    l2 = []
    for i in range(M):

        line = sys.stdin.readline().strip()
        # print(8)
        l = list(map(int, line.split()))
        l2.append(l)
    find_min(N, M, l2)