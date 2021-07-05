import sys

while True :
    string = sys.stdin.readline().rstrip()

    # 0이면 종료
    if string == '0': break

    n = len(string)
    answer = ""

    for i in range(0, n // 2):
        if string[i] == string[n-1-i]:
            continue
        else :
            answer = "no"

    if len(answer) == 0:
        answer = "yes"

    print(answer)