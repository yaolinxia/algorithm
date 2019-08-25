def solution(n, Matrix):
    if n == 1:
        for i in range(1, 4):
            for k in range(0, 4):
                for j in range(0, i):
                    if Matrix[i-j][k]==Matrix[i-j-1][k]:
                        Matrix[i-j-1][k] *= 2
                        Matrix[i-j][k] = 0
                    if Matrix[i-j-1][k] == 0:
                        Matrix[i - j - 1][k] = Matrix[i-j][k]
                        Matrix[i - j][k] = 0
    if n == 2:
        for i in range(2, -1, -1):
            for k in range(0, 4):
                for j in range(0, 3-i):
                    if Matrix[i+j][k]==Matrix[i+j+1][k]:
                        Matrix[i+j+1][k] *= 2
                        Matrix[i+j][k] = 0
                    if Matrix[i+j+1][k] == 0:
                        Matrix[i+j+1][k] = Matrix[i-j][k]
                        Matrix[i+j][k] = 0
    if n == 3:
        for i in range(1, 4):
            for k in range(0, 4):
                for j in range(0, i):
                    if Matrix[i-j][k]==Matrix[i-j-1][k]:
                        Matrix[i-j-1][k] *= 2
                        Matrix[i-j][k] = 0
                    if Matrix[i-j-1][k] == 0:
                        Matrix[i - j - 1][k] = Matrix[i-j][k]
                        Matrix[i - j][k] = 0
    if n == 4:
        for i in range(1, 4):
            for k in range(0, 4):
                for j in range(0, i):
                    if Matrix[i-j][k]==Matrix[i-j-1][k]:
                        Matrix[i-j-1][k] *= 2
                        Matrix[i-j][k] = 0
                    if Matrix[i-j-1][k] == 0:
                        Matrix[i - j - 1][k] = Matrix[i-j][k]
                        Matrix[i - j][k] = 0
    return Matrix


import sys

N = int(sys.stdin.readline().strip())
M = []
for _ in range(N):
    line = sys.stdin.readline().strip()
    # sweets = list(map(int, line.split()))
# print(solution().get_max_sweets(sweets))
    line = list(map(int, line.split()))
    M.append(line)
m = solution(N, M)
for i in range(4):
    print(" ".join(list(map(str, m[i]))))
# print(solution().get_max_sweets([20, 50, 22, 74, 9, 63]))