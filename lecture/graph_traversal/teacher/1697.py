"""
중요한 유형
"""

import sys
from collections import deque

input = sys.stdin.readline

n, k = map(int, input().split())

visited = [-1] * 200000
dq = deque()

dq.append(n)
visited[n] = 0

while dq:
    x = dq.popleft()
    
    if 0 <= x - 1 <= 200000 and visited[x-1] == -1:
        visited[x - 1] = visited[x] + 1
        dq.append(x-1)
    
    if 0 <= x + 1 <= 200000 and visited[x+1] == -1:
        visited[x + 1] = visited[x] + 1
        dq.append(x+1)
    
    if 0 <= x * 2 <= 200000 and visited[x*2] == -1:
        visited[x * 2] = visited[x] + 1
        dq.append(x*2)

print(visited[k])