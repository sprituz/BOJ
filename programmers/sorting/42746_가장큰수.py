def quick_sort(numbers):
    if len(numbers)<=1:
        return numbers
    pivot=numbers[len(numbers)//2]
    less,equal,great=[],[],[]
    for num in numbers:
        if int(str(num)+str(pivot))<int(str(pivot)+str(num)):
            less.append(num)
        elif int(str(num)+str(pivot))>int(str(pivot)+str(num)):
            great.append(num)
        else:
            equal.append(num)
    return quick_sort(less)+equal+quick_sort(great)
    
def solution(numbers):
    answer=quick_sort(numbers)[::-1]
    return str(int("".join(map(str,answer))))