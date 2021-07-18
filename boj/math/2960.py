# 에라토스테네스의 체

'''
1. 2부터 N까지 모든 정수를 적고
2. 아직 지우지 않은 수 중 가장 작은 수 = p (소수)
3. p를 지우고, 아직 지우지 않은 p의 배수를 지운다.
4. 다시 2번으로

n, k가 주어졌을 때 k번째 지워진 수를 구해라

'''
import sys
n, k = map(int, sys.stdin.readline().split())

# 에라토스
check = [False, False] + [True] * (n - 1)
primes = []

cnt = 0
ans = 0
find = False

for i in range(2, n+1):
    if check[i]:
        primes.append(i)
        cnt += 1
        if cnt == k:
            ans = i
            find = True
            break
        for j in range(2*i, n+1, i):
            # 중복으로 지워지는 거 카운팅 방지
            if check[j]:
                cnt += 1
            check[j] = False
            if cnt == k:
                ans = j
                find = True
                break
    if find: break

print(ans)