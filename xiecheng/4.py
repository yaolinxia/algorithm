
def edit_dis(w1, w2):
    m=len(w1)+1; n= len(w2) + 1
    dp = [[0 for i in range(n)] for j in range(m)]
    # dp = []
    # for j in range(m):
    #     for i in range(n):
    #         dp[i][j] = 0
    for i in range(n):
        dp[0][i]=i

    for i in range(m):
        dp[i][0]=i
    for i in range(1,m):
        for j in range(1,n):
            if w1[i-1] == w2[j - 1]:
                dp[i][j] = dp[i-1][j-1]
            else:
                dp[i][j] = min(dp[i][j-1], dp[i-1][j], dp[i-1][j-1]) + 1
    return dp[m-1][n-1]

if __name__ == '__main__':

    # w1 = "携程欢迎您"
    # w2 = "欢迎你程里人"
    # w = "携程欢迎您<ctrip>欢迎你程里人"
    # w1 = input()
    # w2 = input()
    w = input()
    w_split= w.split("<ctrip>")
    w1 = w_split[0]
    w2 = w_split[1]
    print(edit_dis(w1, w2))
