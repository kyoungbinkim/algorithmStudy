from sys import stdin
from heapq import heappush, heappop

n = int(stdin.readline())
vis = set()
next = []
roads = []

start = float('inf')
for _ in range(n):
    s,e = map(int,stdin.readline().split())
    s,e = (s,e) if s<e else (e,s)
    if s not in vis:
        vis.add(s)
        heappush(next, s)
    heappush(roads, (e,s))
vis= None
d = int(stdin.readline())

start = heappop(next)
end = start + d

ans, cnt = 0, 0
cntmap = {}

for _ in range(n):
    e,s = heappop(roads)
    if e-s > d:
        continue
    end = start + d

    while len(next) and  e>end:
        cnt -= cntmap.get(start,0)
        start = heappop(next) if len(next) else s
        end = start + d
    
    cnt += 1 
    cntmap[s] = cntmap.get(s,0) + 1

    ans = max(ans, cnt)

print(ans)
