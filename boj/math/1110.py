# 더하기 사이클

'''
문제 말을 뭐라는 지 못 알아들었고 얼추 규칙을 보니
1. 각 자리 수 합을 더한다
2. 기존 문자 일의 자리 + 1에서 구한 값으로 새로운 수를 만든다
3. 1,2 과정을 원래 입력이 될 때까지 반복한다.
'''

import sys
input = sys.stdin.readline()

num = int(input)
origin = num
cycle = 0

while True:
    tmp = num // 10 + num % 10;  # 십의 자리, 일의 자리
    new = (num % 10) * 10 + tmp % 10  # 일의 자리 -> 십의 자리, tmp를 일의 자리로
    
    cycle += 1

    if new == origin:
        print(cycle)
        break

    num = new # 값 갱신