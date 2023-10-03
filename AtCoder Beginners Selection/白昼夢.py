S=input()
S_check = S[:]
check_list = ['dreamer', 'dream', 'eraser', 'erase']

flag=False

for i in range(len(check_list)):
  for j in range(len(check_list)):
    S_check = S_check.replace(check_list[(i+j)%len(check_list)],'')
  
  if S_check=='':
    flag=True
    break

  S_check = S[:]

if flag:
  print('YES')
else:
  print('NO')

# 解答例
s = input().replace("eraser","").replace("erase","").replace("dreamer","").replace("dream","")
if s:
  print("NO")
else:
  print("YES")