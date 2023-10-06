from sys import stdin

leftDown, rightDown = (1, -1), (1, 1)


n = int(stdin.readline())
board = [list(map(int, stdin.readline().split())) for _ in range(n)]

def makeBoundary(pos, d1, d2):
    up,down, left, right = pos, None, None, None
    b = [[pos, pos], ]
    for i in range(d1):
        b.append([[b[i][0][0] + leftDown[0], b[i][0][1] + leftDown[1]]])

    for i in range(d2):
        b.append([[b[-1][0][0] + rightDown[0], b[-1][0][1] + rightDown[1]]])
        b[i+1].append([b[i][1][0] + rightDown[0], b[i][1][1] + rightDown[1]])
    
    for i in range(d1):
        b[d2+i+1].append([b[d2+i][1][0] + leftDown[0], b[d2+i][1][1] + leftDown[1]])
    # for tmp in b:
    #     print(tmp)
    # print()
    left = (pos[0] + d1 * leftDown[0], pos[1] + d1 * leftDown[1])
    right = (pos[0] + d2 * rightDown[0], pos[1] + d2 * rightDown[1])
    down = (right[0] + d1 * leftDown[0], right[1] + d1 * leftDown[1])

    return [up,left, right, down], b

def calcScore(spots, boundary):
    ans = [0 for _ in range(5)]
    up,left, right, down = spots 
    for i in range(n):
        for j in range(n):
            if up[0] <= i <= down[0] and boundary[i-up[0]][0][1] <= j <= boundary[i-up[0]][1][1]:
                # print(up, down, boundary[i-up[0]][0][1], boundary[i-up[0]][1][1])
                ans[4] += board[i][j]
            elif j <= up[1] and i < left[0]:
                ans[0] += board[i][j]
            elif j > up[1] and i <= right[0]:
                ans[1] += board[i][j]
            elif j < down[1] and i >= left [0]:
                ans[2] += board[i][j]
            elif j >= down[1] and i > right[0]:
                ans[3] += board[i][j]
            else:
                ans[4] += board[i][j]
    
    return max(ans) - min(ans)

ans = float("inf")
for x in range(0, n-1):
    for y in range(1, n-1):

        for d1 in range(1, n-x+1):
            for d2 in range(1, n-x+1):
                if x+d1+d2 >= n or y-d1 < 0 or y+d2 >= n:
                    break

                spot, bound = makeBoundary([x,y], d1, d2)
                ans = min(ans, calcScore(spot, bound))
print(ans)