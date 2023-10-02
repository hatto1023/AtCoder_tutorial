N = int(input())
d=[]
for i in range(N):
  d.append(int(input()))
d = sorted(d, reverse=True)

ans = 0

while len(d) >= 1:
  ans += 1
  d = [i for i in d if i != d[0]]

print(ans)
    
# 解答例
n = int(input())
print(len(set(map(int, [input() for i in range(n)]))))