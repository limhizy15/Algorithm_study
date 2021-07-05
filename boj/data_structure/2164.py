#카드2
import sys
from collections import deque

n = int(input())
dq = deque()
answer = 0

for i in range(n):
    dq.append(i+1)

while len(dq) > 1:
    dq.popleft();
    if len(dq) == 1:
        break
    else:
        tmp = dq[0]
        dq.popleft()
        dq.append(tmp)

answer = dq[0]
print(answer)

