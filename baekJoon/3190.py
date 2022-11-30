from sys import stdin

direction = {"D" : [1,0], "U":[-1,0], "L":[0,-1], "R":[0,1]}

def directionChange(direction, C):
    right = {"D" : "L", "U":"R", "L" : "U", "R":"D"}
    left = {"D" : "R", "U":"L", "L" : "D", "R":"U"}

    if C == "L":
        return left[direction]
    else:
        return right[direction]

def check(snake, pos):
    for i in range(len(snake)):
        if snake[i][0] == pos[0] and snake[i][1] == pos[1]:
            return False
    return True
 
def update(arr, snake, d, n):
    x,y = snake[::-1][0][0] + direction[d][0] , snake[::-1][0][1] + direction[d][1]

    if x<0 or x>=n or y<0 or y>=n:
        return False, 0
    
    if not check(snake, [x,y]):
        return False, 0
    
    snake.append([x,y])
    if arr[x][y] != 'a':
        del snake[0]
        return True, 0
    arr[x][y] = 0
    return True, 1
    

n, appleNum = int(stdin.readline()), int(stdin.readline())
arr, myDirection = [] , "R"

for _ in range(n):
    arr.append([0]*n)

for _ in range(appleNum):
    x,y = map(int, stdin.readline().split())
    arr[x-1][y-1] = "a"

directionChangeNum = int(stdin.readline())
directionChangeList = []
for _ in range(directionChangeNum):
    x,y = stdin.readline().replace("\n","").split()
    directionChangeList.append([int(x), y])
# print(directionChangeList)

snake = [[0,0]]
t = 1
dirInd = 0
apple = 0

while True:
    f, k = update(arr, snake, myDirection, n)
    apple += k
    # print(snake, apple, myDirection, f)
    if not f:
        break

    if directionChangeList[dirInd][0] == t:
        myDirection = directionChange(myDirection, directionChangeList[dirInd][1])
        dirInd += 1
        if len(directionChangeList) == dirInd:
            dirInd -= 1

    t+=1
print(t)