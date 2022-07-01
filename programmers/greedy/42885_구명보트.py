def solution(people, limit):
    people.sort()
    answer = 1
    remain = limit
    left = 0
    right = len(people) - 1
    while left<=right:
        if remain - people[right] >= 0:
            remain -= people[right]
            right -= 1
            continue
        elif remain - people[left] >= 0:
            remain -= people[left]
            left += 1
            continue
        else:
            remain = limit
            answer += 1
            continue


    return answer