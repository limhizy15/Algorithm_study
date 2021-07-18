# 문자열 반복
import sys

tc = int(input())
answer_list = []

for _ in range(tc):
    repeat, word = sys.stdin.readline().split()
    r = int(repeat)
    answer = ""

    for i in range(len(word)):
        tmp = word[i]
        for _ in range(r):
            answer += tmp
    answer_list.append(answer)

for item in answer_list:
    print(item)