import sys

input = sys.stdin.readline

T = int(input())

for _ in range(T):
    N = int(input())
    tree = [[] for _ in range(N + 1)]
    for _ in range(N - 1):
        A, B = map(int, input().split())
        tree[B].append(A)
    node_1, node_2 = map(int, input().split())
    first = [node_1]
    second = [node_2]
    parent_first = node_1
    parent_second = node_2
    while True:
        if tree[parent_first]:
            first.append(tree[parent_first][0])
            parent_first = tree[parent_first][0]
        if tree[parent_second]:
            second.append(tree[parent_second][0])
            parent_second = tree[parent_second][0]
        if len(set(first) & set(second)) == 1:
            print(list(set(first) & set(second))[0])
            break
