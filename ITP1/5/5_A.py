while True:
  H,W = map(int, input().split())
  if H==0 and W==0:
    print()
    break 
  for j in range(H):
    for i in range(W):
      if i==(W-1):
        print("#")
      else:
        print("#", end="")
  print()



  # note
  for i in range(1, 10):
    for j in range(1, 10):        # i の段を横１列に出力する
      val = i * j
      if val < 10:              # １桁の場合は空白入れて調整
        print(' ', end='')
      print(' ', val, end='')
    print()  

  for j in range(4):
    for i in range(8):
      print("#", end="")
    print()