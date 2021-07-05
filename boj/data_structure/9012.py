'''
1. 왼괄호를 스택에 넣음 
2. 입력이 오른괄호이고 스택의 탑이 왼괄호이면 pop
- 왼괄호가 아니면 NO
3. 문자열 끝까지 다 돌았는데 스택이 비지 않으면 NO

'''

import sys

T = int(input())

for i in range(T) :
    ps = sys.stdin.readline().rstrip()

    stack = []
    flag = False

    for i in range(len(ps)) :
        if ps[i] == '(' :
            stack.append(1)
        else :
            if len(stack) > 0 :
                stack.pop()
            else :
                print("NO")
                flag = True
                break
    
    if flag : continue    

    if len(stack) == 0 :
        print("YES")
    else :
        print("NO")


    # print(ps)