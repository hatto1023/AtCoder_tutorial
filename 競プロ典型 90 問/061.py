Q=int(input())
tx=[]
for _ in range(Q):
  t,x=map(int, input().split())
  if t==1:
    tx.insert(0,x)
  elif t==2:
    tx.append(x)
  else:
    print(tx[x-1])

# 解答例
Q = int(input())
from collections import deque
q = deque()
for i in range(Q):
    t, x = map(int,input().split())
    if t == 1:
        q.appendleft(x)
    elif t == 2:
        q.append(x)
    elif t == 3:
        print(q[x - 1])