s=input()
p=input()
index_1=s.find(p[:len(p)//2])
index_2=s.find(p[len(p)//2:])
if index_1 != -1 or index_2 != -1:
  s1=s[index_1:] + s[:index_1]
  s2=s[index_2-(len(p)//2):]+s[:index_2-(len(p)//2)]
  index_11=s1.find(p)
  index_22=s2.find(p)
  if index_11 != -1 or index_22 != -1:
    print("Yes")
  else:
    print("No")
else:
  print("No")


# 解答例
s = input()
p = input()
if p in (s + s):
    print('Yes')
else:
    print('No')