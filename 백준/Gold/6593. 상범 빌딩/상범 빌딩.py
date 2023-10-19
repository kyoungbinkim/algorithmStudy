from sys import stdin
from collections import deque

charMap = {'.': 0, '#': 1}
dir = [
    (1,0,0), (0,-1,0), (0, 1,0), (0,0, 1), (0,0,-1), (-1,0,0)
]

while 1:
    building = []
    visit = set()
    l, n, m = map(int, stdin.readline().split())

    if l == 0 and n == 0 and m == 0:
        break

    for k in range(l):
        building.append([])
        for i in range(n):
            tmp = stdin.readline().removesuffix('\n')
            line = []
            for j in range(m):
                
                if tmp[j] == 'S':
                    start = (k, i, j)
                    que = deque([(start, 0)])
                    visit.add(start)
                    line.append(0)
                elif tmp[j] == 'E':
                    end = (k, i, j)
                    line.append(0)
                else:
                    line.append(charMap[tmp[j]])
            building[k].append(line)
        stdin.readline()
    
    ans = None
    while len(que):
        
        pos, cnt = que.popleft()

        for d in dir:
            dk = pos[0] + d[0]
            dr = pos[1] + d[1]
            dc = pos[2] + d[2]

            if dk < 0 or dr <0 or dc<0 or dk >= l or dr >=n or dc >= m:
                continue

            if building[dk][dr][dc] == 1 or (dk,dr,dc) in visit:
                continue

            if (dk, dr, dc) == end:
                ans = cnt+1
                break

            que.append(((dk,dr,dc), cnt+1))
            visit.add((dk,dr,dc))
        
        if ans:
            break
    
    if ans ==None:
        print("Trapped!")
    else:
        print("Escaped in {} minute(s).".format(ans))