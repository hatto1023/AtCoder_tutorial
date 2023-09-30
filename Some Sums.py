N,A,B = map(int, input().split())

ans = 0

for i in range(1,N+1):
  arr = [int(x) for x in str(i)]
  if A<= sum(arr) & sum(arr)<=B:
    ans += i

print(ans)

# 解答例
n, a, b = map(int, input().split())
ans = 0
for i in range(n+1):
  if a <= sum(list(map(int, list(str(i))))) <= b:
    ans += i
print(ans)