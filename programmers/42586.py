'''
[문제]
기능개발 진도가 100%일 때 서비스에 반영할 수 있다.
각 기능의 개발속도가 모두 다르므로 우선순위에 상관없이 먼저 개발될 수 있으나, 
배포될 때는 우선순위가 높은 기능이 먼저 배포되어야 한다.

[풀이]
1. progresses[i] + speeds[i] * days >= 100인 days를 찾는다.
- 각 기능이 배포될 수 있는 날짜를 days 덱에 저장
2. 배포
1) 현재 days의 맨 앞 요소가 우선순위가 제일 높으므로 배포가능
2) days의 다음 요소들을 탐색하면서 1)에서 구한 것보다 더 빨리 개발완료된 게 있으면 그것도 같이 배포가능
=> 다만 우선순위가 높은 것이 배포되어야 그 다음것도 출력가능하므로 그 다음 요소가 배포불가능 상태면 바로 break
3) 배포될 기능의 수를 나타내는 cnt만큼 days.popleft()로 제거


'''
from collections import deque
import math

def solution(progresses, speeds):
    answer = []
    n = len(progresses)
    days = deque() 
    
    # 걸리는 요일 수 days에 저장
    for i in range(n):
        temp_day = math.ceil((100 - progresses[i]) / speeds[i])
        days.append(temp_day)
    
    while days:
        # 맨 앞부터 배포되어야
        first = days[0]
        cnt = 1
        for i in range(1, len(days)):
            # 배포할 수 없는 상태이므로 break
            if first < days[i]:
                break
            cnt += 1
        
        answer.append(cnt)
        
        # 배포된 수만큼 days에서 제거
        for _ in range(cnt):
            days.popleft()
    
    return answer