T,W = map(int, input().split())

d = [[0] * (W + 1) for _ in range(T + 1)]

tree = []

for i in range(T):
    tree.append(int(input()))

for i in range(1,T+1):
    for j in range(W+1):
        if j == 0:
            d[i][j] = d[i-1][j] + (1 if tree[i - 1] == 1 else 0)
        else:
            if j % 2 == 0:
                d[i][j] = max(d[i - 1][j],d[i-1][j-1]) + (1 if tree[i - 1] == 1 else 0)
            else:
                d[i][j] = max(d[i - 1][j],d[i-1][j-1]) + (1 if tree[i - 1] == 2 else 0)

print(max(d[T]))