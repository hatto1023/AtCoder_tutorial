N,M=map(int, input().split())
array1=[]
ans=0
for i in range(M):
  array1.append([int(x) for x in input().split()])

for i in range(1,N+1):
  num=0
  for j in range(M):
    if i in array1[j]:
      num+=sum([k < i for k in array1[j]])
  if num==1:
    ans+=num
print(ans)

# 解答例
n, m = map(int,input().split())
ans = [0] * n
for i in range(m):
    a, b = map(int,input().split())
    if a < b:
        ans[b - 1] += 1
    else:
        ans[a - 1] += 1

# 自分より小さい頂点が１つしかないものをカウントする
print(ans.count(1))