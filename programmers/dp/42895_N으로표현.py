def solution(N, number):
    answer = 0
    d=[[] for _ in range(9)]
    d[1].append(N)
    d[2].append(N+N)
    d[2].append(N-N)
    d[2].append(N*N)
    d[2].append(N/N)
    d[2].append(int(str(N)*2))
    for i in range(3,9):
        d[i].append(int(str(N)*i))
        for j in range(1,i):
            for k in d[j]:
                for l in d[i-j]:
                    d[i].append(k+l)
                    d[i].append(k-l)
                    d[i].append(k*l)
                    if k==0 or l==0:
                        d[i].append(0)  
                    else:
                        d[i].append(k/l)    
    for i in range(1,9):
        if number in d[i]:
            return i
    
    return -1