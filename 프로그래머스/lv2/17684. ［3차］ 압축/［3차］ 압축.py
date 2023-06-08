def solution(msg):
    answer = []
    dic = {}
    
    for i in range(1,27):
        dic[i] = chr(i+64)
    print(dic)
    
    idx = 0
    while True:
        out = 0
        for i in range(idx, len(msg)):
            if dic[msg[idx:i+1]] not in dic:
                dic[]
        
    
    return answer