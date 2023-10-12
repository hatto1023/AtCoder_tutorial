A,B,C = map(int, input().split())
import math
g=math.gcd(A,B,C)
ans=0
while(A!=g):
  A/=g
  ans+=1
while(B!=g):
  B/=g
  ans+=1
while(C!=g):
  C/=g
  ans+=1
print(ans)

# 解答例
import math
a, b, c = map(int,input().split())
gcd_ab = math.gcd(a, b)
gcd_abc = math.gcd(gcd_ab, c)

ans = (a // gcd_abc - 1) + (b // gcd_abc -  1) + (c // gcd_abc - 1)
print(ans)