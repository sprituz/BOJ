import sys

input = sys.stdin.readline

T = int(input())

t = []
d = [0] * 101

d[1] = 1
d[2] = 1
d[3] = 1

for _ in range(T):
    N = int(input())
    t.append(N)

for i in range(4, max(t) + 1):
    d[i] = d[i - 3] + d[i - 2]

for j in range(T):
    print(d[t[j]])