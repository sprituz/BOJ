from collections import deque
def solution(prices):
    answer = []
    second=0
    queue=deque(prices)
    while queue:
        second=0
        left=queue.popleft()
        for price in queue:
            if left<=price:
                second+=1
            elif left>price:
                second+=1
                break
        answer.append(second)
    return answer