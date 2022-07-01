from collections import deque
n,k=map(int,input().split())
graph=[]
virus=[]
for i in range(n):
    graph.append(list(map(int,input().split())))
s,x,y= map(int,input().split())

dx=[-1,1,0,0]
dy=[0,0,-1,1]


def bfs(graph):
    for j in range(n):
        for k in range(n):
            if graph[j][k]!= 0:
                virus.append((graph[j][k],0,j, k))
    virus.sort(key=lambda x:x[0])
    queue=deque(virus)
    while queue:
        num,sec,x1,y1=queue.popleft()
        if sec==s:
            break
        for i in range(4):
            nx=x1+dx[i]
            ny=y1+dy[i]
            if 0<=nx<n and 0<=ny<n:
                if graph[nx][ny]==0:
                    graph[nx][ny]=graph[x1][y1]
                    queue.append((graph[nx][ny],sec+1,nx,ny))


bfs(graph)
print(graph[x-1][y-1])