# 최대공약수와 최소공배수

'''
두 자연수의 최대공약수GCD, 최소공배수LCM을 출력
'''

# GCD 함수
def gcd(x, y):
    if y == 0: return x
    else: return gcd(y, x % y)

# LCM
def lcm(x, y):
    g = gcd(x, y)
    return g * (x // g) * (y // g)

a, b = map(int, input().split())
print(gcd(a, b))
print(lcm(a, b))