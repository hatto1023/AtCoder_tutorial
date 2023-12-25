n=int(input())
x=[int(x) for x in input().split()]
y=[int(y) for y in input().split()]
x_y=[abs(i-j) for i,j in zip(x,y)]
print(sum(x_y))

p2_Dxy=0
for i in x_y:
  p2_Dxy+=i**2
p2_Dxy=p2_Dxy**(1/2)
print(p2_Dxy)

p3_Dxy=0
for i in x_y:
  p3_Dxy+=i**3
p3_Dxy=p3_Dxy**(1/3)
print(p3_Dxy)

print(max(x_y))