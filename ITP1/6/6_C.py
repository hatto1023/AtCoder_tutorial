n=int(input())
A=[[[0 for i in range(10)] for j in range(3)] for k in range(4)]
for i in range(n):
  b,f,r,v=map(int, input().split())
  A[b-1][f-1][r-1] += v

for i in range(4):
  for j in range(3):
    for k in range(10):
      if k==9:
        print(f" {A[i][j][k]}")
      else:
        print(f" {A[i][j][k]}", end="")
  if i != 3:
    print("####################")