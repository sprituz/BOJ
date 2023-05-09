import sys

input = sys.stdin.readline

N = int(input())

T = [0]
P = [0]

for _ in range(N):
    Ti, Pi = map(int, input().split())
    T.append(Ti)
    P.append(Pi)

d = [0] * 1500002

for i in range(1,N+1):
    d[i] = max(d[i], d[i-1])
    if i + T[i] <= N + 1:
        d[i + T[i]] = max(d[i] + P[i], d[i + T[i]])

print(max(d[:N+2]))