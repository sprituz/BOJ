def solution(name, yearning, photo):
    answer = []
    for p in photo:
        total = 0
        for people in p:
            if people in name:
                total += yearning[name.index(people)]
        answer.append(total)
    return answer