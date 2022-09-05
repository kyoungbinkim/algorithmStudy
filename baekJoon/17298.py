from sys import stdin

listSize = int(stdin.readline())
numList = list(map(int, stdin.readline().split()))
stack = [numList.pop()]
ans = [-1]


def getNum(stack, k):
    lenStack = len(stack)
    for i in range(lenStack-1, -1, -1):
        if stack[i] > k:
            return stack[i]
    return -1 
    

while len(numList)> 0:
    tmp = numList.pop()
    ans.append(getNum(stack, tmp))
    stack.append(tmp)
ans = ans[::-1]
    

for i in range(listSize-1):
    print(ans[i], end=" ")
print(ans[listSize-1])
    
    

