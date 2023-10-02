n=input()
x=[int(i) for i in str(n)]

ans=0
for i in x:
  if i == 1:
    ans+=1
print(ans)


# 解答例
print(input().count('1'))