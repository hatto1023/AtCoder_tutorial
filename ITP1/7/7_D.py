n,m,l=map(int, input().split())
A=[[int(x) for x in input().split()]for i in range(n)]
B=[[int(x) for x in input().split()]for i in range(m)]
C=[[sum([A[i][k]*B[k][j] for k in range(m)])for j in range(l)]for i in range(n)]
for i in range(n):
  for j in range(l):
    if j==l-1:
      print(C[i][j])
    else:
      print(C[i][j], end=" ")