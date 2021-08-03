"""
상하좌우 연결을 본다
2차원 배열 그대로 사용할 것
"""

import sys
from collections import deque

input = sys.stdin.readline

n = int(input())
graph = [input() for i in range(n)]

cnt = []
visited = [[0]* n for _ in range(n)]

dy = [-1, 1, 0, 0]
dx = [0, 0, -1, 1]

def dfs(x, y, number):
    visited[x][y] = number
    for i in range(4):
        X = x + dx[i]
        Y = y + dy[i]
        if X < 0 or X >= n or Y < 0 or Y >= n: continue
        if not visited[X][Y] and graph[X][Y]=='1':
            dfs(X, Y, number)
    

for i in range(n):
    for j in range(n):
        if graph[i][j] == '1' and not (visited[i][j]):
            dfs(i, j, len(cnt)+1)
            # len(cnt) = 0 -> 1 을 채워넣고
            # 1의 개수를 세서 cnt 배열에 넣는다.
            # 그럼 이제 len(cnt)+1 = 2
            count = 0
            for i in range(n):
                count += visited[i].count(len(cnt)+1)
            cnt.append(count)

print(len(cnt))
print(*sorted(cnt), sep='\n')