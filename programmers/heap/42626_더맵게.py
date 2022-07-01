import heapq
def solution(scoville, K):
    answer = 0
    heapq.heapify(scoville)
    while scoville[0]<K:
        answer+=1
        if len(scoville)==1:
            return -1
        min_scovile=heapq.heappop(scoville)
        nextmin_scovile=heapq.heappop(scoville)
        if min_scovile+(nextmin_scovile*2)==0:
            return -1
        heapq.heappush(scoville, min_scovile+(nextmin_scovile*2) )
    return answer