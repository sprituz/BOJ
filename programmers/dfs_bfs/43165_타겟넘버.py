from collections import deque
def solution(numbers, target):
    answer = 0
    queue=deque([(0,0)])

    while queue:
        cnt,num=queue.popleft()
        if cnt<len(numbers):
            queue.append((cnt+1,num+numbers[cnt-1]))
            queue.append((cnt+1,num-numbers[cnt-1]))
        if cnt==len(numbers) and num==target:
            answer+=1
    return answer