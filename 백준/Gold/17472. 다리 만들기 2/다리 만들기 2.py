from sys import stdin
from collections import deque
from heapq import heappush, heappop, heapify

u,d,l,r = (-1,0),(1,0),(0,-1),(0,1)
dir = [u,d,r,l]

n,m = map(int, stdin.readline().split())
b = [list(map(int, stdin.readline().split())) for _ in range(n)]

def update(i,j, idx):
    q = deque([(i,j)])
    b[i][j] = idx
    border = set()
    while q:
        x,y = q.popleft()
        
        for dx, dy in dir:
            nx, ny = x+dx, y+dy
            if 0<=nx<n and 0<=ny<m:
                if  b[nx][ny] == 1:
                    b[nx][ny] = idx
                    q.append((nx,ny))
                elif b[nx][ny] == 0:
                    border.add((x,y))
            else:
                border.add((x,y))
    return border

idx = 2
border = {}
for i in range(n):
    for j in range(m):
        if b[i][j] == 1:
            border[idx] = update(i,j,idx)
            idx += 1

# print(border)
# for l in b:
#     print(l)

links = [[float('inf') for _ in range(idx)] for  _ in range(idx)]

def updateLink(border):
    for x,y in border:
        near = findNear(x,y, b[x][y])
        # print(b[x][y], (x,y),  near)
        for idx, cnt in near:
            links[b[x][y]][idx] = min(links[b[x][y]][idx], cnt)
            links[idx][b[x][y]] = min(links[idx][b[x][y]], cnt)

def findNear (i,j,idx):
    ans = []
    for dx, dy in dir:
        x, y, cnt = i,j, 0
        while True:
            x += dx
            y += dy
            cnt += 1
            if 0<=x<n and 0<=y<m:
                if b[x][y] == idx:
                    break
                elif b[x][y] > 0 and b[x][y] != idx:
                    if cnt >= 3:
                        ans.append((b[x][y], cnt-1))
                    break
            else:
                break
    return ans

for i in range(2, idx):
    updateLink(border[i])

h = []
for i in range(2, idx):
    for j in range(i+1, idx):
        if links[i][j] != float('inf'):
            heappush(h, (links[i][j], i, j))
# print(h)
    

parent = [i for i in range(idx)]

def findP(x):
    if parent[x] == x:
        return x
    parent[x] = findP(parent[x])
    return parent[x]

def Union(x,y):
    x = findP(x)
    y = findP(y)
    if x < y:
        parent[y] = x
    else:
        parent[x] = y

ans = 0
while h:
    cost, a, b = heappop(h)
    if findP(a) != findP(b):
        Union(a,b)
        ans += cost
# print(*[findP(i) for i in range(2, idx)])
for i in range(3, idx):
    if findP(2) != findP(i):
        ans = -1
        break
print(ans) 