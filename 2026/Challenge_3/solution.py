
def DP(total, moedas):
    dp = [0] * (total + 1)
    dp[0] = 1
    for coin in moedas:
        for amount in range(coin, total + 1):
            dp[amount] += dp[amount - coin]
    return dp[total]


if __name__ == '__main__':
    print(DP(10, [1,2,5]))
