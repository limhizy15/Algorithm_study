# 소수

'''
m 이상 n 이하 자연수 중 소수인 것을 골라 이들의 합 & 최솟값은?
소수 없으면 -1만 출력
'''

import sys

m = int(input())
n = int(input())

#  에라
check = [False, False] + [True] * (n - 1)
primes = []

for i in range(2, n+1):
    if check[i]:
        if i >= m:
            primes.append(i)
        for j in range(2*i, n+1, i):
            check[j] = False

if len(primes) == 0:
    print(-1)
else:
    print(sum(primes))
    print(min(primes))

# print(m, n)
