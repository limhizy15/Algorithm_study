# 최소공배수

'''
두 자연수가 주어졌을 때, A와 B의 최소공배수를 구하는 프로그램
T
A, B <= 45000
'''

def gcd(a, b):
    if b == 0:
        return a
    else:
        return gcd(b, a%b)

def lcm(a, b):
    g = gcd(a,b)
    return g * (a // g) * (b // g)

import sys

tc = int(input())
for _ in range(tc):
    a, b = map(int, sys.stdin.readline().split())
    print(lcm(a, b))
    # print(a, b)