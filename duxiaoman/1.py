
def find_max(l):
    n,m,a,b = l[0], l[1], l[2], l[3]
    # h = [[0]*(n) for _ in range(m)]
    h = []
    h_row = [0]*m
    for i in range(n):
        h.append(h_row)
    # for i in range(n):
    #     for j in range(m):
    #         h[i][j] = 0
    # print(h[0][0])
    for i in range(0, n):
        for j in range(0, m):
            print(i,j)
            h[i][j] = ((i+1)*(j+1)) % 10


    for i in range(h[0]):
        print(i)
    # print(h)
    # print(54)

import sys
if __name__ == '__main__':
    l = [4, 5, 3, 3]
    # line = sys.stdin.readline().strip()
    # print(8)
    # l = list(map(int, line.split()))

    find_max(l)
