from collections import deque

dy = [-1, 1, 0, 0]
dx = [0, 0, -1, 1]

def bfs(board, y, x, vis):
    n = len(board)
    m = len(board[0])

    q = deque()
    q.append([y, x])
    vis[y][x] = True
    while q:
        cur = q.popleft()
        cy, cx = cur[0], cur[1]
        for dir in range(4):
            ny = cy + dy[dir]
            nx = cx + dx[dir]
            if ny < 0 or ny >= n or nx < 0 or nx >= m:
                continue
            if vis[ny][nx] or board[ny][nx] == 1:
                continue
            q.append([ny, nx])
            vis[ny][nx] = True

n, m = map(int, input().split())
board = []
for _ in range(n):
    board.append(list(map(int, input())))
vis = [[False] * m for _ in range(n)]

answer = 0
for i in range(n):
    for j in range(m):
        if not vis[i][j] and board[i][j] == 0:
            bfs(board, i, j, vis)
            answer += 1

print(answer)
