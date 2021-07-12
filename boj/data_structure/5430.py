# AC
import sys
from collections import deque

'''
[문제]
R이 들어오면 순서를 뒤집고 D가 들어오면 첫 번째 숫자를 버림

[풀이]
뒤집는 명령나오면 isFront 플래그를 둬서 True <-> False로 방향표시함
덱 만들어서 배열을 넣고 명령을 수행함
문자 버리는 명령나왔을 때 isFront면 popleft 아니면 pop 수행
덱이 비어있는데 버리라고 하면 error출력
'''

tc = int(sys.stdin.readline().rstrip())

isError = False  # 틀린원인1: for문 안에 error플래그를 넣었었음

for _ in range(tc):
    # 입력
    orders = sys.stdin.readline().rstrip()
    n = int(sys.stdin.readline().rstrip())
    arr = sys.stdin.readline().rstrip()[1:-1].split(',')

    isFront = True  # 현재 배열의 방향을 나타내는 플래그 (False면 뒤집힘)
    dq = deque(arr) if n != 0 else deque()

    for order in orders:
        # 방향바꾸는 명령나오면 isFront 값 변경
        if order == 'R':
            if isFront:
                isFront = False
            else:
                isFront = True
        elif order == 'D':  # 버리는 명령
            if len(dq) == 0:  # 비어있으면 error출력
                print('error')
                isError = True
                break
            else:  # 비어있지 않으면 pop
                if isFront:
                    dq.popleft()
                else:
                    dq.pop()

    if not isError:
        if not isFront:
            dq.reverse()

        print('[', end='')
        # 틀린원인2: ','.join(dq)로 출력했었는데 value error 뜸
        # 그래서 그냥 덱 탐색하면서 출력하는 형식으로 바꿈
        for i in range(len(dq)):
            print(dq[i], end='')
            if i != len(dq) - 1:
                print(',', end='')
        print(']')

    isError = False

