"""
격자점에서의 BFS
"""

import sys
from collections import deque

input = sys.stdin.readline

m, n = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(n)]

dy = [-1, 1, 0, 0]
dx = [0, 0, -1, 1]

dq = deque()
for i in range(n):
    for j in range(m):
        if graph[i][j] == 1:
            dq.append((i, j))

answer = 0

# 안 익은 토마토가 있나?
def check(graph, n, m):
    for i in range(n):
        for j in range(m):
            if graph[i][j] == 0:
                return False
    return True

while dq and not(check(graph, n, m)):
    answer += 1
    cnt = len(dq)
    for i in range(cnt):
        x, y = dq.popleft()
        for idx in range(4):
            X = x + dx[idx]
            Y = y + dy[idx]
            
            if X < 0 or X >= n or Y < 0 or Y >= m: continue
            
            if graph[X][Y] == 0:
                dq.append(X, Y)
                graph[X][Y] = 1


if check(graph, n, m):
    print(answer)
else:
    print(-1)
