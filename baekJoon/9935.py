from sys import stdin

def stringBlow(string, c4, n):
    ansStr = ""
    stack = []
    for i in range(len(string)):
        if len(stack) < n-1:
            stack.append(string[i])
            continue
        
        stack.append(string[i])
        if string[i] == c4[n-1]:
            if stack[len(stack)-n:] == c4:
                for _ in range(n):
                    stack.pop()
    for s in stack:
        ansStr += s
    return ansStr

B = list(map(str, stdin.readline().replace('\n', "")))
C = list(map(str, stdin.readline().replace('\n', "")))
S = stringBlow(B, C, len(C))
if S == "":
    print("FRULA")
else:
    print(S)