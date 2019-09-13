def solution(S, h, n):
    count = 0
    for s in S:
        c = n // len(s) + 1
        if (s * c)[:n] == h:
            count += 1
    return count


import sys
if __name__ == "__main__":
    n = int(sys.stdin.readline().strip())
    T = sys.stdin.readline().strip()
    m = int(sys.stdin.readline().strip())
    S = []
    for _ in range(m):
        S.append(sys.stdin.readline().strip())
    print(solution(S, T, n))