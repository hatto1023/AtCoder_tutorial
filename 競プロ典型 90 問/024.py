N,K=map(int, input().split())
A=[int(x) for x in input().split()]
B=[int(x) for x in input().split()]
C=[x-y for (x,y) in zip(A,B)]
C=[abs(i) for i in C]

if sum(C)<=K and (sum(C)-K)%2==0:
  print("Yes")
else:
  print("No")

# 解答例
n, k = map(int,input().split())
a = list(map(int,input().split()))
b = list(map(int,input().split()))

num = 0
for i in range(n):
    num += abs(a[i] - b[i])

if abs(num - k) % 2 == 0 and num <= k:
    print("Yes")
else:
    print("No")