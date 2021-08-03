# BFS와 DFS

"""
방문된 점을 순서대로 출력
근데 작은 것부터..
"""

import sys
from collections import deque

input = sys.stdin.readline

n, m, v = map(int, input().split())
graph = [[] for i in range(n+1)]

dfs_result = []
bfs_result = []

dfs_visited = [0 for i in range(n+1)]
bfs_visited = [0 for i in range(n+1)]

for i in range(m):
    x, y = map(int, input().split())
    graph[x].append(y)
    graph[y].append(x)

def dfs(v):
    dfs_visited[v] = 1
    dfs_result.append(v)
    for next in graph[v]:
        if dfs_visited[next] == 0:
            dfs(next)

def bfs(v):
    dq = deque()
    dq.append(v)
    bfs_visited[v] = 1
    bfs_result.append(v)

    while dq:
        # 1. 원소를 꺼낸다.
        # 2. 자식들에 대해서 반복문을 돌린다.
        # 3. 이 자식들을 방문한 적이 있나?
        # 4. 방문 안 했다면 방문 처리 해주고 큐에 넣자.

        x = dq.popleft()   
        for next in graph[x]:
            if bfs_visited[next] == 0:
                bfs_visited[next] = 1
                bfs_result.append(next)
                dq.append(next)

for i in range(n+1):
    graph[i].sort()

dfs(v)  
bfs(v)

print(dfs_result)
print(bfs_result)