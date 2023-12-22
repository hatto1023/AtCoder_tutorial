r,c=map(int, input().split())
A=[]
for i in range(r):
  a=[int(x) for x in input().split()]
  A.append(a+[sum(a)])
A.append([sum(column) for column in zip(*A)])
for row in A:
  for i,element in enumerate(row):
    if len(row)-1 == i:
      print(element)
    else:
      print(element, end=" ")

# アンパック演算子'*'　転置する方法
# A.append([sum(column) for column in zip(*A)])  