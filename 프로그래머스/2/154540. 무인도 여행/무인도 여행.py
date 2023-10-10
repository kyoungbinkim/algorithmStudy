from collections import deque

dir = [
    (0,1),
    (0,-1),
    (1, 0),
    (-1, 0)
]

def solution(maps):
    answer = []
    n,m = len(maps), len(maps[0])
    board = [[int(x) if x!='X' else 0 for x in line] for line in maps]
    print(board)
    
    for i in range(n):
        for j in range(m):
            if board[i][j]:
                ans = 0
                visit = set([(i,j)])
                que = deque([(i,j)])
                
                while len(que):
                    r,c = que.popleft()
                    ans += board[r][c]
                    board[r][c] = 0
                    for d in dir:
                        dr, dc = r+d[0], c+d[1]
                        
                        if dr<0 or dc <0 or dr >= n or dc >= m or (dr,dc) in visit:
                            continue
                        
                        if board[dr][dc]:
                            visit.add((dr,dc))
                            que.append((dr,dc))
                answer.append(ans)
                
    answer.sort()
    if len(answer) == 0:
        return [-1]
    return answer