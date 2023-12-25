# math.radians(度)
# math.degree(ラジアン)
import math
a,b,C=map(int, input().split())
rad=math.radians(C)
h=b*math.sin(rad)
S=a*h/2
c=math.sqrt(a**2+b**2-2*a*b*math.cos(rad))
L=a+b+c
print(S)
print(L)
print(h)