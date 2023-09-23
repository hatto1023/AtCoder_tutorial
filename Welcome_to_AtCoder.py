a = int(input())
bc = input().split()
b = int(bc[0])
c = int(bc[1])
s = input()

print("{} {}".format(a+b+c,s))

# 解答例
a = int(input())
b, c = map(int, input().split())
s = input()
print("{} {}".format(a+b+c, s))
