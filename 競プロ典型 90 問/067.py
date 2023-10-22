N,K=map(int, input().split())
if N==0:
  exit(print(0))

for i in range(K):
  eight_number=int(str(N),8)
  nine_number=""
  while eight_number>0:
    nine_number += str(eight_number % 9)
    eight_number //= 9
  a=int(nine_number[::-1])

  b=""
  for j in range(len(str(a))):
    if str(a)[j] == "8":
      b+="5"
    else:
      b+=str(a)[j]

  N=int(b)

print(N)


    

# 解答例
def DeciamlToNine(num):
  "10進数を9進数に変換する"
  nine_number = ""
  while num > 0:
      nine_number += str(num % 9)
      num //= 9
  return int(nine_number[::-1])

n, k = map(int,input().split()) # ８進数の数字と交換回数
if n == 0:
    exit(print(0))
eight_number = n
for i in range(k):
    # 8進数を10進数に変換する
    a = int(str(eight_number), 8)

    # 10進数を9進数に変換する
    b = DeciamlToNine(a)

    # 変換した9進数の中に8があれば、5に直す
    c = ""
    for j in range(len(str(b))):
        if str(b)[j] == "8":
            c += "5"
        else:
            c += str(b)[j]
    
    # intに戻す
    c = int(c)
    eight_number = c

print(eight_number)