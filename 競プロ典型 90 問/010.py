N=int(input())
cp=[]
for i in range(N):
  cp.append(list(map(int, input().split())))

Q=int(input())
for _ in range(Q):
  L,R = map(int, input().split())
  A,B = 0,0
  for i in range(L-1,R):
    if cp[i][0] == 1:
      A+=cp[i][1]
    else:
      B+=cp[i][1]
  print("{} {}".format(A,B))

# 解答例
n = int(input())
c, p = [0] * n, [0] * n
for i in range(n):
    c[i], p[i] = map(int,input().split())

one = [0] * (n + 1) # １組の累積和
two = [0] * (n + 1) # ２組の累積和

# 累積和を取っていく
# 1組の p[i] までの和が one[i+1] に入っているようにする
for i in range(n):
    one[i + 1] += one[i]
    two[i + 1] += two[i]

    if c[i] == 1:
        one[i + 1] += p[i]
    else:
        two[i + 1] += p[i]

q = int(input())
for i in range(q):
    l, r = map(int,input().split())
    print(one[r] - one[l - 1], two[r] - two[l - 1])