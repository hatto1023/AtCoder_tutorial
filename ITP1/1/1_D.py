S=int(input())
h=S//60//60
m=S//60-h*60
s=S-h*60*60-m*60
print("{}:{}:{}".format(h,m,s))

# 解答例
s = int(input())
h = s // 3600
m = s % 3600 // 60
s = s % 60
print(f"{h}:{m}:{s}")