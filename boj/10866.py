#덱
import sys
from collections import deque

n = int(input())
dq = deque()

for i in range(n):
    in_ = sys.stdin.readline().rstrip().split()
    # print(in_[0])
    order = in_[0]

    if order == "push_front":
        dq.appendleft(in_[1])
    elif order == "push_back":
        dq.append(in_[1])
    elif order == "pop_front":
        if len(dq) == 0:
            print(-1)
        else:
            print(dq[0])
            dq.popleft()
    elif order == "pop_back":
        if len(dq) == 0:
            print(-1)
        else:
            print(dq[-1])
            dq.pop()
    elif order == "size":
        print(len(dq))
    elif order == "empty":
        if len(dq) == 0:
            print(1)
        else:
            print(0)
    elif order == "front":
        if len(dq) == 0:
            print(-1)
        else:
            print(dq[0])
    elif order == "back":
        if len(dq) == 0:
            print(-1)
        else:
            print(dq[-1])