from itertools import permutations
n= int(input())
a=list(map(int,input().split()))
cnt=list(map(int,input().split()))
op=[]
per=[]
for i in range(4):
    for j in range(cnt[i]):
        op.append(int(i))
per= list(permutations(op,len(a)-1))
my_set=set(per) #중복제거
per=list(my_set)
sum=a[0]
result=[]
for i in per:
    sum=a[0]
    for j in range(1,len(a)):
        if i[j-1]==0:
            sum+=a[j]
        elif i[j-1]==1:
            sum-=a[j]
        elif i[j-1]==2:
            sum*=a[j]
        elif i[j-1]==3:
            if sum<0:
                sum=-sum
                sum//=a[j]
                sum = -sum
            else:
                sum//=a[j]
    result.append(sum)

print(max(result))
print(min(result))
