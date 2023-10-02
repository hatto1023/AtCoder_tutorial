N = int(input())
A = list(map(int, input().split()))
i=0
B = list(map(lambda x: x%2, A))
while(B==N*[0]):
  A = list(map(lambda x: x/2, A))
  B = list(map(lambda x: x%2, A))
  i += 1
print(i)

# 解答例
n = input()
a = list(map(int, input().split()))
ans = float('inf')
for i in a:
  ans = min(ans, len(bin(i)) - bin(i).rfind('1') - 1)
print(ans)