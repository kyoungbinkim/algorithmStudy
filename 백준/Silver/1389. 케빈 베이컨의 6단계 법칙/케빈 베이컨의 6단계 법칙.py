from sys import stdin
from collections import deque

n, m = map(int, stdin.readline().split())

board = [[0 for _ in range(n)] for _ in range(n)]
ans = [[0 for _ in range(n)] for _ in range(n)]

for _ in range(m):
    x,y = map(lambda x: int(x)-1, stdin.readline().split())

    board[x][y] = 1
    board[y][x] = 1


for pos in range(n):
    visit = set([pos])
    que = deque([(pos, 0)])

    while len(que):
        # print(que)
        # input("")
        p ,cnt = que.popleft()
        ans[pos][p] = cnt

        for (idx, num) in enumerate(board[p]):
            if idx not in visit and num>0:
                visit.add(idx)
                que.append((idx, cnt+1))

minAns, idx = float('inf'), -1
for (i, l) in enumerate(ans):
    s = sum(l)
    if s < minAns:
        minAns = s
        idx = i
print(idx+1)
