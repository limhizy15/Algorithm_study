from collections import deque

dy = [-1, 1, 0, 0]
dx = [0, 0, -1, 1]

def bfs(board, y, x, dist):
    n = len(board)
    m = len(board[0])
    q = deque()
    q.append([y, x])
    dist[y][x] = 1
    while q:
        cur = q.popleft()
        cy, cx = cur[0], cur[1]
        for dir in range(4):
            ny = cy + dy[dir]
            nx = cx + dx[dir]
            if ny < 0 or ny >= n or nx < 0 or nx >= m:
                continue
            if dist[ny][nx] > 0:
                continue
            if board[ny][nx] == 0:
                continue
            q.append([ny, nx])
            dist[ny][nx] = dist[cy][cx] + 1

    return dist[n-1][m-1]


n, m = map(int, input().split())

board = []
for _ in range(n):
    board.append(list(map(int, input())))
dist = [[0]*m for _ in range(n)]
# print(board)
answer = bfs(board, 0, 0, dist)

print(answer)
