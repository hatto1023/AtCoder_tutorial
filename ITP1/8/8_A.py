# isalnum(): 文字がすべて英数字なら True を返す
# isalpha(): 文字がすべて英字なら True を返す
# isdigit(): 文字がすべて数字なら True を返す
# islower(): 大小文字の区別がある文字がすべて小文字なら True を返す
# isupper(): 大小文字の区別がある文字がすべて大文字なら True を返す
# lower(): 文字をすべて小文字に変換する
# upper(): 文字をすべて大文字に変換する

STR=[i for i in input().split()]
# print(STR)
for i,str in enumerate(STR):
  if i==len(STR)-1:
    if str.islower():
      print(str.upper())
    elif str.isupper():
      print(str.lower())
    else:
      for ch in str:
        if ch.islower():
          print(ch.upper(),end="")
        elif ch.isupper():
          print(ch.lower(),end="")
        else:
          print(ch,end="")
      print()
  else:
    if str.islower():
      print(str.upper(),end=" ")
    elif str.isupper():
      print(str.lower(), end=" ")
    else:
      for ch in str:
        if ch.islower():
          print(ch.upper(),end="")
        elif ch.isupper():
          print(ch.lower(),end="")
        else:
          print(ch,end="")
      print(end=" ")