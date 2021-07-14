# 단어 뒤집기2

'''
[문제]
문자열s에는 태그, 문자가 존재한다.
태그는 '<'부터 시작하고 '>'에서 끝나는 문자를 말한다.
문자는 영문자와 숫자로 이루어지고 공백으로 구분한다.
s에서 "문자"끼리 뒤집어라

[풀이]
isTag 변수를 둬서 현재 태그에 해당하는 문자인지 체크
word엔 뒤집을 문자를 임시저장하고
answer은 정답을 나타내는 문자열

1. 열린태그를 만나면 지금까지 문자를 뒤집어서 정답에 넣는다.
2. 닫힌태그를 만나면 isTag를 False로 변경
3. 공백을 만났을 때 태그문자가 아니면 뒤집어서 정답에 넣고 태그문자이면 그냥 정답에 넣는다
4. 그 외의 경우에는 태그문자면 answer에, 태그문자가 아니면 word에 더해놓는다

**** 위를 따라오면 word에 문자가 있는 상태에서 탐색이 끝나면 추가가 안된다.. 그래서 for문 종료 후 남은 word를 뒤집어서 추가
**** 이거때문에 고생했다. 4번정도 코드를 갈아엎음..
'''
import sys

string_ = sys.stdin.readline().rstrip()

answer = ""
word = ""
isTag = False

for s in string_:
    # 열린 태그 만나면
    if s == "<":
        isTag = True
        answer += word[::-1] + s  # 태그와 태그 사이의 문자 만날 수 있으므로 word[::-1]추가
        word = ""
    elif s == ">":
        isTag = False
        answer += s
    elif s == " ":
        if not isTag:
            answer += word[::-1] + s
            word = ""
        else:
            answer += s
    else:
        if isTag:
            answer += s
        else:
            word += s

# 마지막 부분 예외처리
answer += word[::-1]
print(answer)