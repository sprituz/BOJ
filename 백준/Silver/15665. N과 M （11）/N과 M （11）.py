from itertools import product

N,M = map(int, input().split())
array = sorted(list(set(list(map(int, input().split())))))

for i in product(array, repeat = M):
    print(* i)