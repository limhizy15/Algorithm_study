import sys

n = int(input())

queue = []
q_size = 0
index = 0

for i in range(n) :
    in_ = sys.stdin.readline().rstrip().split()
    order = in_[0]

    # print(q.myQueue)

    if order == "push" :
        queue.append(in_[1])
    elif order == "pop" :
        if len(queue) == index :
            print(-1)
        else :
            print(queue[index])
            index += 1 # 지우는 대신 다음 인덱스를 가리키도록
    elif order == "size" :
        print(len(queue) - index)
    elif order == "empty" :
        if len(queue) == index :
            print(1)
        else :
            print(0)
    elif order == "front" :
        if len(queue) == index :
            print(-1)
        else :
            print(queue[index])
    elif order == "back" :
        if len(queue) == index :
            print(-1)
        else :
            print(queue[-1])