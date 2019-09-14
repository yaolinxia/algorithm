# 使用动态规划dp
def zuhe(total, money):
#   定义dp[i]为金额为i时的组合数
    dp = [0]*(total+1)
    dp[0] = 1
    for m in money:
        for i in range(total-m+1):
            if dp[i]:
                dp[i+m] += dp[i]
    print(dp)
    print(dp[total])

zuhe(10,[2, 3, 5])
