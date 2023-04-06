from collections import deque
S = input()
T = input()


def bfs(t):
    queue = deque([t])
    while queue:
        node = queue.popleft()
        if node == S:
            print(1)
            return
        if len(node[:len(node) - 1]) >= len(S):
            if node[len(node) - 1] == 'A':
                queue.append(node[:len(node) - 1])
            if node[0] == 'B':
                queue.append(node[::-1][:len(node) - 1])
    print(0)


bfs(T)