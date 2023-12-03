# a.append(1)
# a.extend([1,2,3])

# a = [10, 20, 30, 40, 50]
# print(a)
# print("".join(map(str,a)))
# print(" ".join(map(str,a)))
# print(",".join(map(str,a)))

# a = [5, 4, 3, 2, 1]
# a.sort()
# print(a)
# a.reverse()
# print(a)


n=int(input())
a=[int(x) for x in input().split()]
a.reverse()
print(' '.join(map(str, a)))