# 시험 감독

'''
변수이름은 이쁘게 정하자..
'''

import sys

n = int(sys.stdin.readline())
a = list(map(int, sys.stdin.readline().split()))
b, c = map(int, sys.stdin.readline().split())

ans = 0

for i in range(n):
    a[i] -= b
    ans += 1

    if a[i] > 0:
        ans += a[i] // c

        if a[i] % c != 0:
            ans += 1

print(ans)