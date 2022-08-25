from sys import stdin

def push(q,n):
    q.append(n)

def pop(q):
    if len(q) == 0:
        return -1
    return q.pop(0)

def size(q):
    return len(q)

def empty(q):
    return int(len(q) == 0)

def front(q):
    if empty(q) == 1:
        return -1
    return q[0]

def back(q):
    if empty(q) == 1:
        return -1
    return q[len(q)-1]

queue = []
for _ in range(int(stdin.readline())):
    tmp = stdin.readline().split()
    
    if tmp[0] == "push":
        push(queue, int(tmp[1]))
    elif tmp[0] == "pop":
        print(pop(queue))
    elif tmp[0] == "size":
        print(size(queue))
    elif tmp[0] == "empty":
        print(empty(queue))
    elif tmp[0] == "front":
        print(front(queue))
    elif tmp[0] == "back":
        print(back(queue))