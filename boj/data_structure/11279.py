#최대 힙
import sys
import heapq

'''
methods :
heappush(container, data)
heappop(container)
heapify(x) - 리스트를 heap으로 변환
'''

'''
입력 x가 자연수 - 배열에 x 추가
         0 - 가장 큰 값 출력하고 제거
'''

n = int(input())
hq = []

for i in range(n):
    in_ = sys.stdin.readline().rstrip()
    operator = int(in_)
    # print(operator)
    if operator > 0 :
        heapq.heappush(hq, -operator)
    else:
        if len(hq) == 0:
            print(0)
        else:
            print(-hq[0])
            heapq.heappop(hq)