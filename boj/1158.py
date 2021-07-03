# 1158 요세푸스 문제

from collections import deque

# 입력
n, k = map(int, input().split())

dq = deque()
result = []

for i in range(0, n) :
    dq.append(i+1)

while dq :
    # k번 째 놈 찾기
    for i in range(k-1) :
        # print(list(dq))
        tmp = dq[0]
        dq.popleft()
        dq.append(tmp)

    result.append(dq[0])
    dq.popleft()

# 출력 형식 똑바로 볼 것.
print('<', end = '')
print(', '.join(map(str, result)), end='')
print('>')