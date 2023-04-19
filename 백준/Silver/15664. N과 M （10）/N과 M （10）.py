from itertools import combinations


N,M = map(int, input().split())

s = sorted(list(map(int, input().split())))

array = sorted(set(combinations(s, M)))

for a in array:
    print(*a)