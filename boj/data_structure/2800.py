# 괄호 제거

'''
1. 열린 괄호를 만나면 스택에 해당 인덱스를 저장
2. 닫힌 괄호가 나오면 stack.pop해서 현재 인덱스와 페어로 저장
3. 페어의 조합을 구하고 배열 내부 인덱스들을 참조해서 삭제
4. sort로 정렬해서 출력

**** 중복 제거해줘야함.. 
'''
import sys
from collections import deque
from itertools import combinations
input = sys.stdin.readline()

_str = input.rstrip()

stack = deque()
pair = []
answer = []

# 괄호 쌍 인덱스를 pair에 저장
for i in range(len(_str)):
    if _str[i] == '(':
        stack.append(i)
    elif _str[i] == ')':
        tmp = stack.pop()
        pair.append([tmp, i])

for i in range(len(pair)):
    # pair 수만큼 조합을 ..
    comb = combinations(pair, i+1)

    for data in comb:
        tmp = _str
        for item in data:
            x, y = item
            tmp = list(tmp)
            # 삭제할 괄호를 공백으로 바꿔줌
            tmp[x] = ' '
            tmp[y] = ' '
        answer.append(''.join(tmp).replace(" ", ""))

# 중복 제거 후 정렬
answer = set(answer)
answer = list(answer)
answer.sort()
for ans in answer:
    print(ans)