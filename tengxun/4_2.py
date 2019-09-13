def solution(S, h, n):
    count = 0

    for s in S:
        if set(s) != set(h):
            continue
        len_s = len(s)
        c = n // len_s + 1

        flag = True
        for i in range(c - 1):
            if s != h[i * len_s:(i + 1) * len_s]:
                flag = False
                break
        if flag:
            if h[(c - 1) * len_s:] == s[:(n - c * len_s)]:
                count += 1

    return count


# T = 'abaabaaba'
# S = ['aba','ab','abaaba']
# n = 9
# print(solution(S, T, n))

import sys

if __name__ == "__main__":
    n = int(sys.stdin.readline().strip())
    T = sys.stdin.readline().strip()
    m = int(sys.stdin.readline().strip())
    S = []
    for _ in range(m):
        S.append(sys.stdin.readline().strip())
    print(solution(S, T, n))