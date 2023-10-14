N=int(input())
users,ans=[
],[]
for i in range(N):
  user=input()
  if user not in users:
    ans.append(i+1)
    users.add(user)
print(*ans, sep = "\n")  

# in List O(n)
# in set O(1) 実装がハッシュテーブルであるため

# 解答例
n = int(input())
name, ans = set(), []
for i in range(n):
    s = input()
    if s not in name:
        ans.append(i + 1)
    name.add(s)
print(*ans, sep = "\n")