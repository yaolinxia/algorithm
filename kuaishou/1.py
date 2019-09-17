# 两个字符串求最小操作次数
class Solution:
    def minDistance(self, word1, word2):
        """
        :type word1: str
        :type word2: str
        :rtype: int
        """
        m, n = len(word1), len(word2)
        if m == 0: return n
        if n == 0: return m
        dp = [[0] * (n + 1) for _ in range(m + 1)]  # 初始化dp和边界
        for i in range(1, m + 1): dp[i][0] = i
        for j in range(1, n + 1): dp[0][j] = j
        for i in range(1, m + 1):  # 计算dp
            for j in range(1, n + 1):
                if word1[i - 1] == word2[j - 1]:
                    dp[i][j] = dp[i - 1][j - 1]
                else:
                    dp[i][j] = min(dp[i - 1][j - 1] + 1, dp[i][j - 1] + 1, dp[i - 1][j] + 1)
        return dp[m][n]



# def find_min(s1, s2):


import sys
if __name__ == '__main__':
    # l = [1, 2, 3, 4, 3, 3,1,1]
    # N = int(sys.stdin.readline().strip('\n'))
    s1 = sys.stdin.readline().strip()
    s2 = sys.stdin.readline().strip()
    print(Solution().minDistance(s1, s2))
    # print(8)
    # li = list(map(int, line.split()))
    # li = []
    # for i in range(N):
    #     s = int(sys.stdin.readline().strip('\n'))
    #     li.append(s)
    # s = "2??"
