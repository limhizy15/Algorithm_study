garo = {'a':0, 'b':1, 'c':2, 'd':3, 'e':4, 'f':5, 'g':6, 'h':7 }

def isPossible(y,x):
    if y >= 8 or y < 0 or x >= 8 or x < 0:
        return False
    else:
        return True

loc = input() # 나이트의 위치
temp = loc[0] # 열
x = garo[temp] # 열을 숫자로
y = int(loc[1])-1 

# 상,하,좌,우 2칸씩
dy = [-2, 2, 0, 0]
dx = [0, 0, -2, 2]

answer = 0

# 상하좌우 2칸씩 탐색
for dir in range(4):
    ny = y + dy[dir]
    nx = x + dx[dir]
    if not isPossible(ny, nx):
        continue
    # 양옆, 위아래 체크 후 이동 가능하면 +1
    if 0 <= dir <= 1:
        if isPossible(y, x-1):
            answer += 1
        if isPossible(y, x+1):
            answer += 1
    elif 2 <= dir <= 3:
        if isPossible(y-1, x):
            answer += 1
        if isPossible(y+1, x):
            answer += 1

print(answer)
