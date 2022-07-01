def solution(number, k):
    tmp=0
    while k>0:
        for i in range(tmp,len(number)-1):
            if int(number[i])==9:
                continue
            if int(number[i])<int(number[i+1]):
                tmp=i
                number=number[:i]+number[i+1:]
                k-=1
                if tmp!=0:
                    tmp=i-1
                else:
                    tmp=0
                break
                
            elif i==len(number)-2 and k!=0:
                number=number[0:len(number)-k]
                k=0
                break
    return number