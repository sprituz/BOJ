def solution(n, lost, reserve):
    lost.sort()
    reserve.sort()
    tmp=lost[:]
    for i in tmp:
        if i in reserve:
            lost.remove(i)
            reserve.remove(i)
    answer=n-len(lost)
    for i in lost:
        if i-1 in reserve:
            reserve.remove(i-1)
            answer+=1
            continue
        elif i+1 in reserve:
            reserve.remove(i+1)
            answer+=1
            continue
    return answer