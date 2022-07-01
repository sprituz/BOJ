def solution(answers):
    one=[1,2,3,4,5]
    two=[2, 1, 2, 3, 2, 4, 2, 5]
    three=[3, 3, 1, 1, 2, 2, 4, 4, 5, 5]
    score={1:0,2:0,3:0}
    for i in range(len(answers)):
        if one[i%5]==answers[i]:
            try:score[1]+=1
            except KeyError: score[0]=1 
        if two[i%8]==answers[i]:
            try:score[2]+=1
            except KeyError: score[1]=1 
        if three[i%10]==answers[i]:
            try:score[3]+=1
            except KeyError: score[2]=1 
    return [k for k, v in score.items() if max(score.values())==v ]