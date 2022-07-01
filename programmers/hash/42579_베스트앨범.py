def solution(genres, plays):
    answer = []
    album={}
    count={}
    for i in range(len(genres)):
        if genres[i] not in album:
            count[genres[i]]=plays[i]
            album[genres[i]]=[]
            album[genres[i]].append([plays[i],i])
        else:
            count[genres[i]]+=plays[i]
            album[genres[i]].append([plays[i],i]) 
    ordered_count=sorted(count.items(),key=lambda x:x[1], reverse=True)
    for i in album.keys():
        album[i].sort(key=lambda x:x[1])
        album[i].sort(key=lambda x:x[0],reverse=True)
    for genre, play in ordered_count:
        if len(album[genre])>=2:
            answer.append(album[genre][0][1])
            answer.append(album[genre][1][1])
        else:
            answer.append(album[genre][0][1])
    return answer