import sys

k = 0
n = 0
Y = [[0]*(9+3) for _ in range(100)]


def production():
    dp = [None]*100
    for i in range(100):
        dp[i] = Y[i][1:]

    for line in sys.stdin:
        k, n = map(int, line.split())

        if k == 0:
            print(100.0)
            continue

        for i in range(k+1):
            dp[0][i] = 1

        dp[0][k+2] = dp[0][-1] = 0

        for i in range(1, n):
            for j in range(k+1):
                dp[i][j] = dp[i-1][j-1] + dp[i-1][j] + dp[i-1][j+1]
            dp[i][k+2] = dp[i][-1] = 0

        num = sum(dp[n-1][:k+1])

        denom = pow(k+1, n)

        print("{:.9f}".format(100.0*num/denom))


if __name__ == "__main__":
    production()
