alpha_list=[0]*26
while True:
  try:
    str = input()
    if not str:
      break
    for ch in str:
      num = ord(ch.lower()) - ord('a')
      if num<0 or 25<num:
          continue
      alpha_list[num]+=1
  except EOFError:
      break
for i,num in enumerate(alpha_list):
  print(f"{chr(i+97)} : {num}")