while True:
  st=input()
  if st == "-":
    break
  m=int(input())
  for i in range(m):
    h=int(input())
    st=st[h:]+st[:h]
  print(st)