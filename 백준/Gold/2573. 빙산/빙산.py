from collections import deque
import sys

input = sys.stdin.readline
N,M = map(int, input().split())
array = [list(map(int, input().split())) for _ in range(N)]
answer = 0
count = 0
dx = [-1,1,0,0]
dy = [0,0,-1,1]


def bfs(x, y, visited):
    queue = deque([(x,y)])
    visited[x][y] = True
    while queue:
        node = queue.popleft()
        for i in range(4):
            if 1 <= node[0] + dx[i] < N - 1 and 1 <= node[1] + dy[i] < M -1:
                if array[node[0] + dx[i]][node[1] + dy[i]] != 0 and not visited[node[0] + dx[i]][node[1] + dy[i]]:
                    queue.append((node[0] + dx[i], node[1] + dy[i]))
                    visited[node[0] + dx[i]][ node[1] + dy[i]] = True


while True:
    visited = [[False] * M for _ in range(N)]
    temp = [[0] * M for _ in range(N)]
    count = 0
    for i in range(1,N-1):
        for j in range(1,M-1):
            if not visited[i][j] and array[i][j] != 0:
                count += 1
                if count > 1:
                    break
                bfs(i,j, visited)

    if count > 1:
        print(answer)
        break
    elif count == 0:
        print(0)
        break
    answer += 1
    for i in range(1,N-1):
        for j in range(1,M-1):
            if array[i][j] != 0:
                zero_count = 0
                for k in range(4):
                    if array[i + dx[k]][j + dy[k]] == 0:
                        zero_count += 1
                if array[i][j] - zero_count < 0:
                    temp[i][j] = 0
                else:
                    temp[i][j] = array[i][j] - zero_count
    array = temp