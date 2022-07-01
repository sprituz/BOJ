from collections import deque
def solution(n, edge):
    answer = 0
    distance=[0]*(n+1)
    visited=[0]*(n+1)
    vertex=[[] for _ in range(n+1)]
    for v in edge:
        vertex[v[0]].append(v[1])
        vertex[v[1]].append(v[0])
    queue=deque([[1,0]])
    visited[1]=1
    while queue:
        node,dis=queue.popleft()
        for i in vertex[node]:
            if visited[i]==0:
                queue.append([i,dis+1])
                distance[i]=dis+1
                visited[i]=1
    max_distance=max(distance) 
    return distance.count(max_distance)