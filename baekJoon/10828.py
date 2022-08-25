from sys import stdin
def push(stack, n):
    stack.append(n)

def pop(stack):
    if len(stack) == 0:
        return -1
    return stack.pop()

def size(stack):
    return len(stack)

def empty(stack):
    return int(len(stack) == 0)

def top(stack):
    if empty(stack):
        return -1
    return stack[len(stack)-1]

stck = []
cmdNum = int(input())
for _ in range(cmdNum):
    tmp = stdin.readline().split()

    if tmp[0] == "push":
        push(stck, int(tmp[1]))
    elif tmp[0] == "pop":
        print(pop(stck))
    elif tmp[0] == "size":
        print(size(stck))
    elif tmp[0] == "empty":
        print(empty(stck))
    elif tmp[0] == "top":
        print(top(stck))

