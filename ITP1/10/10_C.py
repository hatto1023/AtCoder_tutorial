import math
while True:
  n=int(input())
  if n==0:
    break
  s=[int(x) for x in input().split()]
  m=sum(s)/n
  a=0
  for i in s:
    a+=(i-m)**2
  a=math.sqrt(a/n)
  print(a)