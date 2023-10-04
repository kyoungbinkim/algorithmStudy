from sys import stdin

dir = [
    (0,1),(0,-1),(1,0),(-1,0)
]

n = int(stdin.readline())

studentMap = {}
studentOrd = []

board = [[0 for _ in range(n)] for _ in range(n)]

for _ in range(n*n):
    tmp = list(map(int, stdin.readline().split()))

    studentOrd.append(tmp[0])
    studentMap[tmp[0]] = set(tmp[1:])

def calc(pos, num):
    ans = [0,0]

    if board[pos[0]][pos[1]]:
        return (-1, -1)

    for d in dir:
        dr,dc = pos[0]+d[0], pos[1]+d[1]

        if dr<0 or dc<0 or dr>=n or dc>=n:
            continue

        if board[dr][dc] == 0:
            ans[1] += 1
        else:
            ans[0] += int(board[dr][dc] in studentMap[num])
    
    return tuple(ans)

sat = 0
for num in studentOrd:
    ans = (-1, -1)
    ansPos = (-1,-1)
    for i in range(n):
        for j in range(n):
            newAns = calc((i,j), num)

            if newAns > ans:
                ansPos = (i,j)
                ans = newAns
    
    board[ansPos[0]][ansPos[1]] = num
    # for l in board:
    #     print(l)
    # print()

for i in range(n):
    for j in range(n):
        tmp = 0
        for d in dir:
            dr,dc = i+d[0], j+d[1]

            if dr<0 or dc < 0 or dr >= n or dc>= n:
                continue
            
            if board[dr][dc] in studentMap[board[i][j]]:
                tmp += 1
        
        if tmp != 0:
            sat += 10 ** (tmp-1)
print(sat)