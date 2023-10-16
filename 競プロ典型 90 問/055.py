N,P,Q=map(int, input().split())
A=[int(x) for x in input().split()]
ans=0
import itertools
for i in itertools.combinations(A,5):
  an=1
  for j in range(5):
    an=an*i[j]%P
  if an%P==Q:
    ans+=1
print(ans)

# 解答例
from itertools import combinations
N, P, Q = map(int,input().split())
A = list(map(int,input().split()))
ans = 0
for a, b, c, d, e in combinations(A, 5):
    if a % P * b % P * c % P * d % P * e % P == Q: 
        ans += 1
print(ans)