# 소수&팰린드롬

'''
N보다 크거나 같고 소수이고 팰린드롬인 수 중 가장 작은

*** 처음에 한번 틀린 원인 : MAX값을 입력 n의 최댓값으로 둬서
백만의 소수&팰린드롬 수를 찾지 못했다. 그래서 일단 MAX값을 2배로 둬서 해결했다.
*** 다른 사람의 코드를 보니 백만의 경우에 나올 수 있는 수를 아예 예외처리해서 구했더라..
'''

def is_palin(n):
    s = str(n)
    if s == s[::-1]:
        return True
    else:
        return False

n = int(input())
MAX = 2000000

check = [False, False] + [True] * (MAX-1)
primes = []
ans = 0

for i in range(2, MAX+1):
    if check[i]:
        primes.append(i)  # 소수다
        # 팰린드롬 판별
        if i >= n:
            if is_palin(i):
                ans = i
                break
        # 지우기
        for j in range(2*i, MAX+1, i):
            check[j] = False

print(ans)