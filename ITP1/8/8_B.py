while(True):
  str=input()
  if int(str) == 0:
    break
  sum=0
  for d in str:
    sum+=int(d)
  print(sum)