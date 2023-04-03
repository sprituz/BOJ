import sys

input = sys.stdin.readline

N = int(input())
array = []

for i in range(N):
    age, name = input().split()
    array.append((i,int(age),name))

array.sort(key=lambda x: (x[1], x[0]))

for a in array:
    print(a[1], a[2])
