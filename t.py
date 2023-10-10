import sys

def calculate_percentage(num, total):
    return "{:.9f}".format((num / total) * 100)

def calculate_tight_words():
    dp = [[0]*(10) for _ in range(100)]
    inputs = list(map(int, sys.stdin.readline().strip().split()))

    while inputs:
        k, n = inputs[0], inputs[1]

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

        tight_words = sum(dp[n-1][:k+1])
        total_words = pow(k+1, n)

        print(calculate_percentage(tight_words, total_words))

        inputs = list(map(int, sys.stdin.readline().strip().split()))

if __name__ == "__main__":
    calculate_tight_words()
