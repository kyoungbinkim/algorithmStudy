from sys import stdin
from copy import deepcopy

c = [5 for _ in range(5)]
board = [list(map(int, stdin.readline().split())) for _ in range(10)]
global globalAns
globalAns = float('inf')

def search(b, colorPapers):
    global globalAns
    if sum([sum(l) for l in b]) == 0:
        globalAns = min(globalAns, 5*5 - sum(colorPapers))
        return 5*5 - sum(colorPapers)
    if 5*5 - sum(colorPapers) >= globalAns:
        return globalAns
    ans = float("inf")
    FLAG = False
    for i in range(10):
        for j in range(10):
            if b[i][j]:
                for dist in range(5, 0 , -1):
                    if i+dist > 10 or j + dist > 10 or colorPapers[dist-1] == 0:
                        continue

                    s = 0
                    for r in range(i, i+dist):
                        s += sum(b[r][j: j+dist])
                    
                    if s == dist * dist:
                        newB = deepcopy(b)
                        newC = colorPapers.copy()
                        newC[dist-1] -=1

                        for r in range(i, i+dist):
                            newB[r][j: j+dist] = [0 for _ in range(dist)]
                        # for nb in newB:
                        #     print(nb)
                        # print()

                        ans = min(ans, search(newB, newC)) 
                FLAG = True
                break
        if FLAG:
            break
    return ans

ret = search(board, c) 
print(ret if ret != float('inf') else -1)