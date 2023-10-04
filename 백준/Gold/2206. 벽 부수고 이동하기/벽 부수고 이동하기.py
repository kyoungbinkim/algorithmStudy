from sys import stdin
from collections import deque

dir = [
    (0,1),
    (0,-1),
    (1, 0),
    (-1,0)
]

n, m = map(int, stdin.readline().split())

board = [[int(x) for x in stdin.readline().removesuffix('\n')] for _ in range(n)]

visit = set([((0,0), False)])
que = deque([((0,0), False, 1)]) # pos, isBreak, cnt


while len(que):
    pos, flag, cnt = que.popleft()
    # print(pos, flag, cnt)

    if pos == (n-1,m-1):
        print(cnt)
        exit(0)

    for d in dir:
        dr, dc = pos[0] + d[0], pos[1] + d[1]

        if dr <0 or dc < 0 or dr >= n or dc >= m or ((dr,dc), flag) in visit:
            continue

        if board[dr][dc] == 1 and flag:
            continue

        if dr == n-1 and dc == m-1:
            print(cnt+1)
            exit(0)
        
        que.append(((dr,dc), board[dr][dc] == 1 or flag, cnt+1))
        visit.add(((dr,dc), board[dr][dc] == 1 or flag))
print(-1)

