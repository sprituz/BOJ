def solution(clothes):
    answer = 1
    hash={}
    for clothes_name, clothes_type in clothes:
        if clothes_type not in hash:
            hash[clothes_type]=1
        elif clothes_type in hash:
            hash[clothes_type]+=1
    for i in hash.values():
        answer*=(i+1)
    return answer-1