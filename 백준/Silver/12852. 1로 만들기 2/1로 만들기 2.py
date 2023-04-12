N = int(input())

count = 0
dp = [[1] for _ in range(N + 1)]
if N >= 2:
    dp[2] = [2,1]
if N >= 3:
    dp[3] = [3,1]

for i in range(4, N + 1):
    if i % 3 == 0:
        dp[i] = [i] + dp[i // 3]
    if i % 2 == 0:
        if dp[i] != [1]:
            if len(dp[i]) > len([i] + dp[i // 2]):
                dp[i] = [i] + dp[i // 2]
        else:
            dp[i] = [i] + dp[i // 2]
    if dp[i] != [1]:
        if len(dp[i]) > len([i] + dp[i - 1]):
            dp[i] = [i] + dp[i - 1]
    else:
        dp[i] = [i] + dp[i - 1]

print(len(dp[N]) - 1)
print(*dp[N])