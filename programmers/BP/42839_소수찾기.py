def permutation(arr, n):
    result = []
    if n == 0:
        return [[]]
    for i, elem in enumerate(arr):
        for PermResult in permutation(arr[:i] + arr[i + 1:], n - 1):
            result += [[elem] + PermResult]
    return result

def solution(numbers):
    number = []
    answer= []
    for i in range(1,len(numbers)+1):
        number+=permutation(numbers,i)
    for i in number:
        if int("".join(i)) not in answer:
            j=int("".join(i)) 
            for i in range(2,j):
                if j%i==0:
                    break
                elif i==j-1:
                    answer.append(j)
            if j==2:
                answer.append(j)
            
    return len(answer)