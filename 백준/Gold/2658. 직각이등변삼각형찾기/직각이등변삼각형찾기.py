from sys import stdin

board = [[int(x) for x in stdin.readline().removesuffix('\n')] for _ in range(10)]

points, pointCnt = [], 0

for i in range(10):
    if sum(board[i]) == 0:
        continue

    for j in range(10):
        if board[i][j]:
            points.append([(i,j)])
            break
    
    for j in range(9, -1, -1):
        if board[i][j]:
            points[-1].append((i,j))
            break
    
    if len(points) and points[-1][0] == points[-1][1]:
        pointCnt += 1
    
    if len(points) and sum(board[i][points[-1][0][1]: points[-1][1][1]+1]) != points[-1][1][1]+1 - points[-1][0][1]:
        print(0)
        exit(0)
            
# print(pointCnt,points)

def isValid(line):

    validDirSet = set([(1,0), (1,1), (1,-1)])

    dir = (line[1][0] - line[0][0], line[1][1] - line[0][1])
    # print(line)
    # print(dir)
    if dir not in validDirSet:
        return (False, None)
    
    for i in range(len(line)-1):
        if line[i+1][0] != line[i][0] + dir[0]:
            return (False, None)
        if line[i+1][1] != line[i][1] + dir[1]:
            return (False, None)
    return (True, dir)
    
if len(points) == 1:
    print(0)
    exit()
    
elif pointCnt == 2:
    # print(pointCnt)
    if len(points) % 2 == 0:
        print(0)
        exit(0)
    
    lup, ldown = [x[0] for x in points[:len(points)//2+1 ]], [x[0] for x in points[len(points)//2:]]
    rup, rdown = [x[1] for x in points[:len(points)//2+1 ]], [x[1] for x in points[len(points)//2:]]
    lupFlag, lupDir = isValid(lup)
    ldownFlag, ldownDir = isValid(ldown)
    
    rupFlag, rupDir = isValid(rup)
    rdownFlag, rdownDir= isValid(rdown)
    # print(lupFlag, lupDir)
    # print(ldownFlag, ldownDir)
    # print(rupFlag, rupDir )
    # print(rdownFlag, rdownDir)
    if (lupFlag and ldownFlag and rupFlag and rdownFlag) == False:
        print(0)
        exit(0)
    
    if (lupDir != ldownDir and rupDir == rdownDir) or (lupDir == ldownDir and rupDir != rdownDir):
        mid = points[len(points) // 2]
        if mid[0][1] != points[0][0][1]:
            ans = [mid[0]]
        else:
            ans = [mid[1]]
        ans += [points[0][0], points[-1][0]]
        # print(ans)
        ans.sort()
        for (x,y) in ans:
            print(x+1,y+1)
    else: 
        print(0)
        exit(0)
    exit(0)
elif pointCnt == 1:
    l, r = [x[0] for x in points], [x[1] for x in points]
    lFlag, lDir = isValid(l)
    rFlag, rDir = isValid(r)
    # print(lFlag, lDir)
    # print(rFlag, rDir)
    if (lFlag and rFlag) == False:
        print(0)
        exit(0)
    
    if points[0][0] == points[0][1]:
        ans = [points[0][0]] + points[-1]
    else:
        ans = [points[-1][0]] + points[0]
    ans.sort()
    for (x,y) in ans:
        print(x+1,y+1)
    exit(0)
print(0)


