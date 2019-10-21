


"""
第一行两个整数 n 和 W ，用空格隔开，表示想要过河的人数，以及在除去船夫的情
况下独木舟最多能搭载的重量。(1 <= n <= 10000，1 <= W <= 2000000000) 第
2行到n+1行，每行一个整数，表示第i个人的重量。(1 <= wi <= min(W,1000000000))。
3 6
1
2
3
"""

def min_nums(mans, W):
    mans = sorted(mans)
    mans_small = []
    for c in mans:
        if c <= W:
            mans_small.append(c)
        else:
            break
    if len(mans_small) == 2:
        if mans_small[0] + mans_small[1] > W:
            return 2
        else:
            return 1
    if n == 1:
        return 1
    if mans[0] + mans[n - 1] <= W:
        mans[n - 1] += mans[0]
        return mans(n - 1, W, mans[1:]) + 1
    else:
        return mans(n - 1, W, mans[:n - 2]) + 1
    # print(int(len(mans_small)+1)//2)


import sys
if __name__ == '__main__':
    line = sys.stdin.readline().strip()
    l = list(map(int, line.split(" ")))
    # l = line.split(' ')
    n = l[0]
    W = l[1]
    mans = []

    for i in range(n):
        p = int(input())
        mans.append(p)
    # print(mans)

    # W = 6
    # mans = [2, 1, 3]
    c = min_nums(mans,W)
    print(c)
    # print(2)
