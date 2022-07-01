def solution(n, times):
    start=0
    end = max(times)*n
    while start<=end:
        tmp=0
        mid=(start+end)//2
        for time in times:
            tmp+=mid//time
            if tmp>=n:
                end=mid-1
                answer=mid
                break
        if tmp<n:
            start=mid+1

    return answer