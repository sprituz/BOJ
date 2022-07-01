from collections import deque
import sys
input = sys.stdin.readline


def rotate(num,com):
  d1=num//1000
  d2=(num%1000)//100
  d3=(num%100)//10
  d4=num%10
  if com == "L":
    return d2*1000+d3*100+d4*10+d1
  elif com=="R":
    return d4 * 1000 + d1 * 100 + d2 * 10 + d3

def bfs(A, B, T):
  for i in range(len(A)):
    queue=deque([[A[i],""]])
    visited=set()
    visited.add(A[i])
    while queue:
      node=queue.popleft()
      if node[0]==B[i]:
        print(node[1])
        break
      if node[0]*2>9999 and node[0]*2 not in visited:
        queue.append([(node[0]*2)%10000,node[1]+"D"])
        visited.add((node[0]*2)%10000)
      else:
        if (node[0] * 2) not in visited:
          queue.append([(node[0] * 2), node[1] + "D"])
          visited.add(node[0] * 2)
      if node[0]==0 and 9999 not in visited:
        queue.append([9999,node[1]+"S"])
        visited.add(9999)
      else:
        if node[0]-1 not in visited:
          queue.append([node[0]-1,node[1]+"S"])
          visited.add(node[0]-1)
      L=rotate(node[0],"L")
      R=rotate(node[0],"R")
      if L not in visited:
        queue.append([L,node[1]+"L"])
        visited.add(L)
      if R not in visited:
        queue.append([R, node[1] + "R"])
        visited.add(R)

T = int(input())
A = []
B = []
for i in range(T):
  a, b = map(int, input().split())
  A.append(a)
  B.append(b)
bfs(A,B,T)