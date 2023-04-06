N = int(input())
T = [0]
P = [0]
for _ in range(N):
    ti, pi = map(int, input().split())
    T.append(ti)
    P.append(pi)

d = [0] * 21


for i in range(1, N+1):
    d[i] = max(d[i], d[i - 1])
    d[T[i] + i] = max(d[i] + P[i], d[T[i] + i])

print(max(d[:N+2]))