from collections import deque
from sys import stdin
from itertools import combinations

dir = [
    (0,1),
    (0,-1),
    (1,0),
    (-1,0),
]

n, m = map(int, stdin.readline().split())
board, virus, walls = [], [], 0

for i in range(n):
    board.append(list(map(int, stdin.readline().split())))
    for j in range(n):
        if board[i][j] == 2:
            board[i][j] = 0
            virus.append((i,j))
        elif board[i][j] == 1:
            walls += 1

# for b in board:
#     print(b)
# print()
# print(virus)

def BFS(idxs):
    total = walls + len(virus)
    virus_ = [virus[i] for i in idxs]

    visit = set(virus_)
    que = deque()
    for pos in virus_:
        que.append((pos, 0))
    
    while len(que):
        pos, cnt = que.popleft()
        if pos not in virus:
            total += 1
        if total == n*n:
            break

        for d in dir:
            dr, dc = pos[0] + d[0], pos[1] + d[1]

            if (dr,dc) in visit or dr <0 or dc <0 or dr >=n or dc >= n:
                continue
                
            if board[dr][dc] == 1:
                continue

            visit.add((dr,dc))
            que.append(((dr,dc), cnt+1))
    # print(total, cnt)
    return cnt if total == n*n else float("inf")

ans = float("inf")
for idxs in combinations(range(len(virus)), m):
    # print(idxs)
    
    newAns = BFS(idxs)

    ans = newAns if newAns < ans else ans

print(ans if ans != float('inf') else -1)
