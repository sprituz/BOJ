def solution(participant, completion):
    completion.sort()
    participant.sort()
    for i in range(len(completion)):
        if completion[i]!=participant[i]:
            return participant[i]
        elif i==len(completion)-1:
            return participant[len(completion)]