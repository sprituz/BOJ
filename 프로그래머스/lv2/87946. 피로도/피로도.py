answer = 0
def back(k,visited,depth,dungeons):
    global answer
    if depth == len(dungeons):
        return
    else:
        for i in range(len(dungeons)):
            if k >= dungeons[i][0] and visited[i] == False:
                visited[i] = True
                answer = max(answer, depth+1)
                back(k-dungeons[i][1],visited,depth+1,dungeons)
                visited[i] = False
        

def solution(k, dungeons):
    global answer
    back(k,[False]*len(dungeons),0,dungeons)
    return answer