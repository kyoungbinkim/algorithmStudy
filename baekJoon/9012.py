

def isValid(s):
    stack = []
    for i in range(len(s)):
        if s[i] == "(":
            stack.append(s[i])
        else:
            if len(stack) == 0:
                return "NO"
            stack.append(s[i])
            t1,t2 = stack.pop(), stack.pop()
            if t1 != ")" or t2 != "(":
                return "NO"
    if len(stack) != 0:
        return "NO"
    return "YES"

num = int(input())
for _ in range(num):
    print(isValid(input()))