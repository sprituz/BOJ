from collections import deque
def distance(a,b):
    count=0
    for i in range(len(a)):
        if a[i]!=b[i]:
            count+=1
    return count
def bfs(n,visited,words,target):
    queue=deque([[n,0]])
    while queue:
        node=queue.popleft()
        if node[0]==target:
            return node[1]
        for i in range(len(words)):
            if visited[i]==0 and distance(node[0],words[i])==1:
                queue.append([words[i],node[1]+1])
                visited[i]=1
        
def solution(begin, target, words):
    answer = 0
    visited=[0]*len(words)
    if target not in words:
        return 0
    answer=bfs(begin,visited,words,target)
    
    return answer