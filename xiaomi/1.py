# class So
# def maxP(pri):
#     cand = []
#     max_p = 0
#     if len(pri) <= 1:
#         return max_p
#     for i in range(len(pri)):
#         l =


class Solution(object):
    def max_p(self, money):
        if not money:
            return 0
        len_p = len(money)
        dp = [[0]*len_p for _ in range(3)]
        for k in range(1, 3):
            p_max = -money[0]
            for i in range(1, len_p):
                p_max = max(p_max, dp[k-1][i-1]-money[i])
                dp[k][i] = max(dp[k][i-1], money[i]+p_max)
        return dp[-1][-1]

import sys
if __name__ == '__main__':
    line = sys.stdin.readline().strip()
    # 把每一行的数字分隔后转化成int列表
    mon = list(map(int, line.split()))

    print(Solution().max_p(mon))


