n=int(input())
score1=0
score2=0
for _ in range(n):
  str1, str2 = input().split()
  if str1 == str2:
      score1+=1
      score2+=1
  elif str1 < str2:
    score2+=3
  elif str1 > str2:
    score1+=3
print(f"{score1} {score2}")