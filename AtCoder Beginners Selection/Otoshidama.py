N, Y = map(int, input().split())

flag = False

for x in range(N+1):
  for y in range(N+1):
    for z in range(N+1):
      if x+y+z == N:
        if 10000*x+5000*y+1000*z == Y:
          flag = True
          print("{} {} {}".format(x,y,z))
          break
      if x==N & y==N & z==N:
        print("-1 -1 -1")
    if flag:
      break
  if flag:
    break

# 解答例
n, y = map(int, input().split())
for i in range(n + 1):
  for j in range(n - i + 1):
    if i * 10000 + j * 5000 + (n - i - j) * 1000 == y:
      print(i, j, n - i - j)
      exit()
print("-1 -1 -1")