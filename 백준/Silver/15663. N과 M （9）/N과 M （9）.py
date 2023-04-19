from itertools import permutations


N,M = map(int, input().split())

s = list(map(int, input().split()))

array = sorted(set(permutations(s, M)))

for a in array:
    print(*a)