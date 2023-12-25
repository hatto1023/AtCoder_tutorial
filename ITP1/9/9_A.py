W=input()
ans=0
while True:
  st=input().split()
  if st[0]=="END_OF_TEXT":
    break
  for i in st:
    if W==i.lower():
      ans+=1
print(ans)