n=int(input())
cards = [[False for i in range(13)] for j in range(4)]
pattern = ["S", "H", "C", "D"]

for _ in range(n):
  ch,rank=input().split()
  rank=int(rank)
  cards[pattern.index(ch)][rank-1] = True

for i in range(4):
  for j in range(13):
    if cards[i][j] == False:
      print(pattern[i], j+1)

# for i in range(1,53):
#     if not (i in cards):