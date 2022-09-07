from sys import stdin

Priority = {"+":2, "-" :2, "*":1, "/":1, ")":0, "(":-1}

# 괄호
def posfix_step1(prefix):
    stack = []
    for i in range(len(prefix)):
        p = Priority.get(prefix[i])
        stack.append(prefix[i])
        if p == 0:
            t= 0 
            tmp = []
            while Priority.get(t) != -1:
                t= stack.pop()
                tmp.insert(0,t)
            del tmp[0]
            tmp = posfix(tmp,1)
            tmp = posfix(tmp,2)
            stack.append(tmp[0])
            
    return stack
        
def posfix_step2(prefix):
    stack = []
    for i in range(len(prefix)):
        stack.append(prefix[i])

        if len(stack)>=3:
            p = Priority.get(stack[len(stack)-2])
            if p == 1:
                a,b,c = stack.pop(), stack.pop(), stack.pop()
                stack.append(c+a+b)
    return stack

def posfix(prefix, prior):
    stack = []
    for i in range(len(prefix)):
        stack.append(prefix[i])

        if len(stack)>=3:
            p = Priority.get(stack[len(stack)-2])
            if p == prior:
                a,b,c = stack.pop(), stack.pop(), stack.pop()
                stack.append(c+a+b)
    return stack

p = list(map(str, stdin.readline().replace('\n','')))
p = posfix_step1(p)
p = posfix(p,1)
p = posfix(p,2)
print(p[0])