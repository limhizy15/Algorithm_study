# 이항 계수 1
'''
이항계수 N K를 구하는 프로그램 작성
nCk이거..
'''

'''
n! / k!(n-k)!
'''
memo = []

def factorial(n):
    if n == 0:
        return 1

    return n * factorial(n-1)

n, k = map(int, input().split())

print(factorial(n) // (factorial(k) * factorial(n-k)))


#
# print(n)
# print(k)