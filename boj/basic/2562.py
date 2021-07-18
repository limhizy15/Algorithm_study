# 최댓값
import sys

num = []

for _ in range(9):
    num.append(int(input()))

_max = 0
ans = 0

for i in range(9):
    if num[i] > _max:
        _max = num[i]
        ans = i+1

print(_max)
print(ans)
