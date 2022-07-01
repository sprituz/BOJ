def solution(brown, yellow):
    cell_sum=brown+yellow
    for i in range(3,int((brown+yellow)**(1/2))+1):
        if cell_sum%i==0:
            if (i-2)*(cell_sum//i-2)==yellow:
                return [cell_sum//i,i]