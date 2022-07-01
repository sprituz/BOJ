def solution(jobs):
    jobs.sort(key=lambda x: (x[0], x[1]))
    length = len(jobs)
    answer =jobs[0][1]
    time=jobs[0][0]+jobs[0][1]
    del jobs[0]
    jobs.sort(key=lambda x: (x[1], x[0]))
    while jobs:
        for i in range(len(jobs)):
            if jobs[i][0] <= time:
                time += jobs[i][1]
                answer += time - jobs[i][0]
                del jobs[i]
                break
            elif i==len(jobs)-1:
                time+=1

    return answer // length