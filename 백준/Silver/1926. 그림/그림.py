from collections import deque
import sys

input = sys.stdin.readline

dx = [-1,1,0,0]
dy = [0,0,-1,1]


def bfs(x,y):
    global max_area, n, m
    queue = deque([(x,y)])
    visited[x][y] = True
    cnt = 0
    while queue:
        node = queue.popleft()
        cnt += 1
        for i in range(4):
            if 0 <= node[0] + dx[i] < n and 0 <= node[1] + dy[i] < m:
                if paint[node[0] + dx[i]][node[1] + dy[i]] == 1 and not visited[node[0] + dx[i]][node[1] + dy[i]]:
                    queue.append((node[0] + dx[i], node[1] + dy[i]))
                    visited[node[0] + dx[i]][node[1] + dy[i]] = True
    max_area = max(max_area, cnt)


n, m = map(int, input().split())
paint = [list(map(int, input().split())) for _ in range(n)]
visited = [[False] * m for _ in range(n)]
paint_count = 0
max_area = 0

for i in range(n):
    for j in range(m):
        if paint[i][j] == 1 and visited[i][j] == False:
            paint_count += 1
            bfs(i,j)

print(paint_count)
print(max_area)