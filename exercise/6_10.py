n = int(input())

num = []
for _ in range(n):
    num.append(int(input()))

num.sort()
num.reverse()
for i in range(len(num)):
    print(num[i], end = ' ')
