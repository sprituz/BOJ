from collections import deque
def solution(bridge_length, weight, truck_weights):
    answer = 0
    crossed=[]
    truck_num=len(truck_weights)
    wait=deque([1,j] for j in truck_weights)
    crossing=deque()
    while len(crossed)<truck_num:
        answer+=1
        for i in range(len(crossing)):
            crossing[i][0]+=1
        while len(crossing)>0 and crossing[0][0]>bridge_length:
            crossed.append(crossing.popleft())
        sum_crossing=sum(y for x,y in crossing)
        if len(wait)>0 and len(crossing)<bridge_length and sum_crossing+wait[0][1]<=weight:
            crossing.append(wait.popleft())
    return answer