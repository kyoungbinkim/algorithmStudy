from sys import stdin

bracketMap = {')': '(', ']': '['}
numMap = {"(":2, "[":3, ")": 2, "]": 3}

bracketStr = stdin.readline().replace('\n', '')

class Stack:
    def __init__(self, str):
        self.str = str
        self.stack = []


    def update(self, c):
        if c in ['(', '[']:
            self.stack.append(c)
        else:
            num = 0
            if len(self.stack) == 0:
                return False

            while len(self.stack)>0 and type(self.stack[-1]) == int:
                num += self.stack.pop()
            
            num = 1 if num == 0 else num

            if len(self.stack)==0 or self.stack[-1] != bracketMap[c]:
                return False

            self.stack.append(numMap[self.stack.pop()] * num )

        return True
        
    def clac(self):
        for s in self.str:
            if not self.update(s):
                self.stack = [0]
                break
        
        ans = 0
        for s in self.stack:
            if type(s) == int:
                ans += s
            else:
                self.stack = [0]
                return
        self.stack = [ans]

stack = Stack(bracketStr)
stack.clac()
print(stack.stack[0])