def solution(progresses, speeds):
    answer = []
    days=[0]*len(progresses)
    for i in range(len(progresses)):
        while progresses[i]<100:
            progresses[i]+=speeds[i]
            days[i]+=1
    #print(days)
    max_days=days[0]
    tmp=1
    for i in range(1,len(days)):
        if max_days>=days[i]:
            tmp+=1
        else:
            max_days=days[i]
            answer.append(tmp)
            tmp=1
    answer.append(tmp)
    return answer