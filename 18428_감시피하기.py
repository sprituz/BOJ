from itertools import combinations
from collections import deque
n=int(input())
graph=[]
graph1=[[0]*n for _ in range(n)]
blank=[]
wall=[]
teacher=[]
result="NO"
dx=[-1,1,0,0]
dy=[0,0,-1,1]
for i in range(n):
    graph.append(list(input().split()))

for i in range(n):
    for j in range(n):
        if graph[i][j]=='X':
            blank.append((i,j))
        if graph[i][j] == 'T':
            teacher.append((i, j))
wall=list(combinations(blank,3))


def watch(nx,ny,graph1,dir):
    if dir==0:
        while nx>=0:
            if graph1[nx][ny]=="S":
                return False
            if graph1[nx][ny]=="O":
                return True
            nx-=1
        return True
    elif dir==1:
        while nx<n:
            if graph1[nx][ny]=="S":
                return False
            if graph1[nx][ny]=="O":
                return True
            nx+=1
        return True
    elif dir==2:
        while ny>=0:
            if graph1[nx][ny]=="S":
                return False
            if graph1[nx][ny]=="O":
                return True
            ny-=1
        return True
    elif dir==3:
        while ny<n:
            if graph1[nx][ny]=="S":
                return False
            if graph1[nx][ny]=="O":
                return True
            ny+=1
        return True

def find(map):
    for x,y in teacher:
        for i in range(4):
            if not watch(x,y,map,i):
                return False
    return True

for (a,b),(c,d),(e,f) in wall:
    for i in range(n):
        for j in range(n):
            graph1[i][j] = graph[i][j]

graph1[a][b] = 'O'
graph1[c][d] = 'O'
graph1[e][f] = 'O'
if find(graph1):
    result="YES"
        break

print(result)


