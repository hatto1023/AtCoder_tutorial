H,W=map(int, input().split())
A=[]
for i in range(H):
  A.append(list(map(int, input().split())))

import numpy as np
A = np.array(A)

for i in range(H):
  for j in range(W):
    if j==W-1:
      print(np.sum(A[i,:])+np.sum(A[:,j])-A[i,j])
    else:
      print(np.sum(A[i,:])+np.sum(A[:,j])-A[i,j], end=" ")

# 累積和・前処理・包除原理
# 解答例
h, w = map(int,input().split())
a = []
for i in range(h):
    a.append(list(map(int,input().split())))
ans = [[0] * w for _ in range(h)]

# 縦の列ごとに合計を前計算する
y = [0] * w
for i in range(w):
    cnt = 0
    for j in range(h):
        cnt += a[j][i]
    y[i] = cnt

# 縦の列ごとに合計を前計算する
x = [0] * h
for i in range(h):
    cnt = 0
    for j in range(w):
        cnt += a[i][j]
    x[i] = cnt

for i in range(h):
    for j in range(w):
        ans[i][j] = (x[i] + y[j]) - a[i][j]

for i in range(h):
    print(*ans[i])