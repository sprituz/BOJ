import sys

input = sys.stdin.readline

N = int(input())

tri = []
dp = []

for i in range(N):
    tri.append(list(map(int, input().split())))
    dp.append([0] * len(tri[i]))
    if i == 0:
        dp[i] = [tri[0][0]]
    else:
        for j in range(len(tri[i])):
            if j == 0:
                dp[i][j] = dp[i - 1][j] + tri[i][j]
            elif j == len(tri[i]) - 1:
                dp[i][j] = dp[i - 1][j-1] + tri[i][j]
            else:
                dp[i][j] = max(dp[i - 1][j-1] + tri[i][j], dp[i - 1][j] + tri[i][j])

print(max(dp[N - 1]))