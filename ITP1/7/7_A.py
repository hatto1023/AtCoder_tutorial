while(True):
  m,f,r=map(int, input().split())
  if m==-1 and f==-1 and r==-1:
    break
  if m==-1 or f==-1:
    print("F")
    continue
  total=m+f
  if total>=80:
    print("A")
  elif total>=65:
    print("B")
  elif total>=50:
    print("C")
  elif total>=30:
    if r>=50:
      print("C")
    else:
      print("D")
  else:
    print("F")