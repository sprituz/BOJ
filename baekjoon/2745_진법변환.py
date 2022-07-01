N,B=input().split()
answer=0
for i in range(len(N)-1,-1,-1):
  if 65<=ord(N[i])<=90:
    answer+=(ord(N[i])-55)*(int(B)**(len(N)-1-i))
  else:
    answer += (int(N[i])) * (int(B) ** (len(N) - 1 - i))
print(answer)