N=int(input())
TX=[]
tx=[]
for i in range(N):
  tx=[int(x) for x in input().split()]
  TX.append(tx)
  tx=[]

print(TX[0,N-1])

# 解答例
# コード
n = int(input())
for i in range(n):
  t,x,y = map(int,input().split())
  if (x + y) > t or (x + y + t) % 2:
    print("No")
    exit()
print("Yes")