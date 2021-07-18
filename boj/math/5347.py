# LCM

'''
a, b의 최소 공배수를 출력
'''

def gcd(x, y):
    if y == 0:
        return x
    else:
        return gcd(y, x%y)

def lcm(x, y):
    g = gcd(x, y)
    return g * (x // g) * (y // g)

import sys
tc = int(input())
for _ in range(tc):
    a, b = map(int, sys.stdin.readline().split())
    print(lcm(a, b))