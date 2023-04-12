N = int(input())

array = list(map(int, input().split()))

dp = [0] * N
dp[0] = array[0]

for i in range(1, N):
    for j in range(i-1, -1, -1):
        if array[j] < array[i]:
            dp[i] = max(dp[i], dp[j] + array[i])
    if dp[i] == 0:
        dp[i] = array[i]

print(max(dp))