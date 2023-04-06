R, C, K = map(int, input().split())
maps = [list(input()) for _ in range(R)]
dx = [-1,1,0,0]
dy = [0,0,-1,1]
answer = 0


def back(x, y, depth):
    global answer
    if depth == K and x == 0 and y == C - 1:
        answer += 1
        return
    for i in range(4):
        if 0 <= x + dx[i] < R and 0 <= y + dy[i] < C:
            if maps[x + dx[i]][y + dy[i]] == '.':
                maps[x + dx[i]][y + dy[i]] = 'T'
                back(x + dx[i], y + dy[i], depth + 1)
                maps[x + dx[i]][y + dy[i]] = '.'


maps[R - 1][0] = 'T'
back(R - 1,0,1)
print(answer)