from collections import deque
def bfs(n,graph,visited):
    queue=deque([graph[n]])
    visited[n]=1
    while True:
        if not queue:
            return 1
        network=queue.popleft()
        for i in range(len(network)):
            if visited[i]==0 and network[i]==1:
                queue.append(graph[i])
                visited[i]=1
        
def solution(n, computers):
    answer = 0
    visited=[0]*n
    for i in range(n):
        if visited[i]==0:
            if bfs(i,computers,visited) == True:
                answer+=1
    return answer