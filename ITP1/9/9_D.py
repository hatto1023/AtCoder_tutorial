str=input()
q=int(input())
for _ in range(q):
  order=input().split()
  a,b=map(int, order[1:3])
  if order[0] == "replace":
    str=str[:a]+order[3]+str[b+1:]
  elif order[0] == "reverse":
    str=str[:a]+str[a:b+1][::-1]+str[b+1:]
  elif order[0] == "print":
    print(str[a:b+1])