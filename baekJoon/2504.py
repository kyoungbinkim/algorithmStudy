bracketMap = {')': '(', ']': '['}
numMap = {")": 2, "]": 3}


class STACK:
    def __init__(self, arr) -> None:
        self.stack = arr

    def get(self):
        if len(self.stack) == 0:
            return None
        return self.stack[len(self.stack)-1]

    def get2(self):
        if len(self.stack) >= 2:
            return self.stack[len(self.stack)-2]
        return None

    def pop(self):
        if len(self.stack) == 0:
            return None
        tmp = self.stack[len(self.stack)-1]
        del self.stack[len(self.stack)-1]
        return tmp

    def push(self, n):
        self.stack.append(n)

    def getStack(self):
        return self.stack
    
    def clear(self):
        self.stack = []

    def update(self):
        intType = type(1)
        tmp = self.stack.copy()
        self.clear()
        for s in tmp:
            if type(s) == intType and type(self.get()) == intType:
                num = self.pop() + s
                self.push(num)
            elif self.get2() == bracketMap.get(s) and type(self.get()) == intType and self.get2() != None:
                num = self.pop()
                l = self.pop()
                num = num * numMap[s]
                self.push(num)
            else:
                self.push(s)


def check(string):
    stack = []
    result = []
    for s in string:
        if bracketMap.get(s) == None:
            stack.append(s)
            result.append(s)
        else:
            if len(stack) == 0:
                return False, None
            if bracketMap[s] != stack[len(stack)-1]:
                return False, None
            del stack[len(stack)-1]

            if bracketMap[s] == result[len(result)-1]:
                del result[len(result)-1]
                result.append(numMap[s])
            else:
                result.append(s)
    if len(stack) > 0:
        return False, None
    return True, result

                
if __name__ =="__main__":
    string = input()
    flag, out = check(string)
    if not flag:
        print(0)
    else:
        intType = type(1)
        stack = STACK(out)

        while len(stack.getStack()) > 1:
            stack.update()
        print(stack.getStack()[0])