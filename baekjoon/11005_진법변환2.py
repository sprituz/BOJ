N,B=input().split()
answer=""
num=int(N)
remain=[]
while num>=int(B):
  remain.append(num % int(B))
  num=num//int(B)
if 10<=num<=35:
  answer+=chr(num+55)
else:
  answer+=str(num)
for i in range(len(remain)-1,-1,-1):
  if 10<=remain[i]<=35:
    answer=answer+chr(remain[i]+55)
  else:
    answer=answer+str(remain[i])
print(answer)