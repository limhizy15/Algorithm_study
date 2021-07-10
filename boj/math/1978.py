# 소수 찾기

'''
N개의 수 중 소수의 개수 출력
에라토스테네스의 체 사용
'''

MAX = 1000

n = int(input())
numbers = list(map(int, input().split()))

# 소수 아닌 애들 지워서 기록할 배열
# True면 지워진 애들
checked = [False] * (MAX + 1)
checked[0] = True
checked[1] = True

for i in range(2, MAX+1):
    if not checked[i]:
        j = i + i
        while j <= MAX:
            checked[j] = True
            j += i

answer = 0

for item in numbers:
    if not checked[item]:
        answer += 1

print(answer)
# print(numbers)