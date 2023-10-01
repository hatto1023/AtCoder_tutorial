n=int(input())
a=[int(x) for x in input().split()]
Alice=0
Bob=0
for i in range(n):
  if i % 2 == 0:
    Alice += max(a)
    a.remove(max(a))
  else:
    Bob += max(a)
    a.remove(max(a))

print(Alice-Bob)

# 解答例
n = int(input())
a = sorted(list(map(int, input().split())), reverse=True)
print(sum(a[::2]) - sum(a[1::2]))