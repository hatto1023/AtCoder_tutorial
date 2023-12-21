n,m=map(int, input().split())
A=[[int(x) for x in input().split()] for i in range(n)]
b=[int(input()) for i in range(m)]
for a in A:
  print(sum([i*j for i,j in zip(a,b)]))