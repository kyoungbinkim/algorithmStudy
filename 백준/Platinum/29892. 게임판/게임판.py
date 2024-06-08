from sys import stdin
from collections import deque

c2n = {'.': 0 , '1':1, '2':2, }
dir = [
    (0,1),
    (0,-1),
    (1,0),
    (-1,0)
]

n,m,k = map(int, stdin.readline().split())
h = k//2

b = [list(map(lambda x: c2n[x], stdin.readline().strip())) for _ in range(n)]

ans = float('inf')
for sr in range(h, n-h):
    for sc in range(h, m-h):
        one, two = 0, 0
        q = deque([(sr,sc)])
        visit = set([(sr,sc)])

        while len(q):
            r,c = q.popleft()

            if abs(sr-r) > h or abs(sc-c) > h:
                continue

            if b[r][c] == 1:
                one += abs(sr-r) + abs(sc-c)
            elif b[r][c] == 2:
                two += abs(sr-r) + abs(sc-c)

            for dr, dc in dir:
                nr, nc = r+dr, c+dc

                if abs(nr - sr) > h or abs(nc - sc) > h or (nr, nc) in visit:
                    continue

                visit.add((nr,nc))
                q.append((nr,nc))
            
        ans = min(ans, abs(one-two))
print(ans)
