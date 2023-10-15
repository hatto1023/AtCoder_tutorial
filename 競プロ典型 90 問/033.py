H,W=map(int, input().split())
ans=0
ans_H=0
ans_W=0

if H>=W:
  H,W=W,H
if H<2:
  ans_H=1
if W<2:
  ans_W=1

while(H>1):
  H/=2
  ans_H+=1
while(W>1):
  W/=2
  ans_W+=1

ans+=ans_H*ans_W
print(ans)

# 解答例
h, w = map(int,input().split())
if min(h, w) == 1:
    print(max(h, w))
else:
    print(((h + 1) // 2) * ((w + 1) // 2))