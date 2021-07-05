# 스택
import sys

stack = []

def push(n) :
    stack.append(n)

def pop() :
    if len(stack) == 0 :
        return -1
    else :
        return stack.pop()

def size() :
    return len(stack)

def empty() :
    if len(stack) == 0 :
        return 1
    else :
        return 0

def top() :
    if len(stack) == 0 :
        return -1
    else :
        return stack[-1]

n = int(input())

for i in range(n) :
    # input 썼더니 시간초과
    input_ = sys.stdin.readline().rstrip().split()
    order = input_[0]

    # 출력형식 틀렸대서 함수로 구현하니 괜찮아짐
    if order == "push" :
        push(input_[1])
    elif order == "pop" :
        print(pop())
    elif order == "size" :
        print(size())
    elif order == "empty" :
        print(empty())
    else :
        print(top())    
    