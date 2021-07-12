# N번째 큰 수

'''
[문제]
NxN 배열에 수가 주어질 때, n번째 큰 수를 구해라

[풀이]
처음생각: 다 힙큐에 넣고 n번 pop해서 구할까? n 최댓값이 1500이라 안돌아갈 것 같다.
그러면 한 줄씩 힙큐에 넣으면서 요소를 n개 남기면 n번째 큰 수를 구할 수 있겠다.
- 처음줄은 일단 힙큐에 push
- 다음줄부터는 힙큐에 push하고 요소가 n개 남을때까지 pop
다 하고나면 현재 힙큐의 루트가 n번째 큰 수가 된다.
'''

import heapq
import sys

n = int(sys.stdin.readline().rstrip())

arr = []

for _ in range(n):
    # 한 줄 입력받아서 힙큐에 push
    row = list(map(int, sys.stdin.readline().rstrip().split(" ")))
    for item in row:
        heapq.heappush(arr, item)
    # 숫자 n개만 남기고 pop
    while len(arr) > n:
        heapq.heappop(arr)

# 남은 요소가 n개이므로 이 상태에서 힙큐의 루트가 n번째 큰 수임!
# 헷갈렸던 것 : n번째 큰 수가 뭔말인지.. 이해하는데 시간 걸림
print(heapq.heappop(arr))
