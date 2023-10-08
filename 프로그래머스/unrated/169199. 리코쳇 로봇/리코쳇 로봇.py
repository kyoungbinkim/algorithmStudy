from collections import deque

dir = [
    (1,0), (-1,0), (0,1), (0,-1)
]    

def solution(board):
    
    numBoard = []
    n,m = len(board), len(board[0])
    for (b, i) in zip(board, range(len(board))):
        tmp = []
        for ( c, j) in zip(b, range(len(b))):
            if c == '.':
                tmp.append(0)
            elif c == 'D':
                tmp.append(1)
            elif c == 'G':
                tmp.append(0)
                end = (i,j)
            elif c == 'R':
                tmp.append(0)
                start = (i,j)
        numBoard.append(tmp)
    print(numBoard)
    print(start,end)
    
    visit = set([start])
    que = deque([(start, 0)])
    
    while len(que):
        pos, cnt = que.popleft()
        
        for d in dir:
            now = pos
            next = (pos[0] + d[0], pos[1] + d[1])
            
            while True:
                if next[0] < 0 or next[1] < 0 or next[0] >= n or next[1]>=m:
                    break
                
                if numBoard[next[0]][next[1]] == 1:
                    break
                
                now = next
                next =  (next[0] + d[0], next[1] + d[1])
            
            if now == end:
                return cnt+1
            
            if now not in visit:
                visit.add(now)
                que.append((now, cnt+1))
    
    return -1