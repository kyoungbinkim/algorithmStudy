from sys import stdin
from collections import deque

n,m,k = map(int, stdin.readline().split())
virus = set(list(map(int, stdin.readline().split())))
logs = [tuple(map(int, stdin.readline().split())) for _ in range(m)]
logs.sort()

LO = deque(logs)
# print(logs)
for idx in range(1, n+1):
    if idx not in virus:
        continue
    
    logs = deque(LO)
    ans = set([idx])

    bt, bs, be = logs.popleft()
    udpate = set()
    logs.append((bt, bs, be))
    if bs in ans:
        udpate.add(be)
        if be not in virus:
            continue

    for _ in range(m-1):
        
        t, s, e = logs.popleft()
        logs.append((t,s,e))

        if t == bt:
            if s in ans:
                udpate.add(e)
                if e not in virus:
                    break
            bt, bs, be = t, s, e
        else:
            ans  = ans.union(udpate)
            if s in ans:
                udpate.add(e)
                if e not in virus:
                    break
            bt, bs, be = t, s, e
    ans = ans.union(udpate)
    # print(ans)
    if virus == ans:
        print(idx)
        break
        
