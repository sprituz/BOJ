from itertools import combinations

def solution(number):
    answer = 0
    for n in list(combinations(number, 3)):
        if sum(n) == 0:
            answer += 1
    return answer