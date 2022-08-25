def pop(stack):
    if len(stack) == 0:
        return -1
    tmp = stack.pop()
    return tmp

def sget(stack):
    if len(stack) == 0:
        return -1
    return stack[len(stack)-1]

size = int(input())
arr = list(range(1, size+1))
stack,ans = [], ""

for _ in range(size):
    tmp = int(input())
    while sget(stack) != tmp:
        if len(arr) == 0:
            break
        stack.append(arr[0])
        ans = ans + "+"
        del arr[0]
        if len(arr) == 0:
            break
        
    
    p = pop(stack)
    ans = ans +"-"
    if p != tmp:
        ans = "NO"
        break
if ans == "NO":
    print(ans)
else:
    for s in ans:
        print(s)