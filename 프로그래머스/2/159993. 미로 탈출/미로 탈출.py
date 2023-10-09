from collections import deque

dir = [
    (0,1),(0,-1),(1,0),(-1,0)
]

def solution(maps):
    answer = -1
    board = []
    n,m = len(maps), len(maps[0])
    for (line, i) in zip(maps, range(len(maps))):
        tmp = []
        for (c, j) in zip(line, range(len(line))):
            if c == 'X':
                tmp.append(1)
            else:
                tmp.append(0)
            
            if c == 'S':
                start =(i,j)
            elif c == 'L':
                lever = (i,j)
            elif c == 'E':
                end = (i,j)
        board.append(tmp)
    # print(board, start, lever, end)
    
    visit = set(start)
    que = deque([(start, 0)])
    
    
    while len(que):
        pos, cnt = que.popleft()
        
        for d in dir:
            
            dr,dc = pos[0]+d[0] , pos[1] + d[1]
            
            if dr<0 or dc <0 or dr >= n or dc >= m or (dr,dc) in visit:
                continue
            
            if board[dr][dc] == 1:
                continue
            
            if (dr,dc) == lever:
                
                answer = cnt+1
                break
            
            visit.add((dr,dc))
            que.append(((dr,dc), cnt+1))
        
        if answer >= 0:
            break
    
    if answer < 0:
        return -1
    
    visit = set(lever)
    que = deque([(lever, 0)])
    
    endFlag = False
    while len(que):
        pos, cnt = que.popleft()
        
        for d in dir:
            
            dr,dc = pos[0]+d[0] , pos[1] + d[1]
            
            if dr<0 or dc <0 or dr >= n or dc >= m or (dr,dc) in visit:
                continue
            
            if board[dr][dc] == 1:
                continue
            
            if (dr,dc) == end:
                
                answer += (cnt + 1)
                endFlag = True
                break
            
            visit.add((dr,dc))
            que.append(((dr,dc), cnt+1))
        
        if endFlag:
            break
    
    
    return answer if endFlag else -1