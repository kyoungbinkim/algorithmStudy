from sys import stdin
from math import sqrt

def updateG(G, plist, ind):
    
    for i in range(ind):
        tmp = (plist[i][0] - plist[ind][0]) **2 + (plist[i][1] - plist[ind][1])**2
        tmp = sqrt(tmp)
        G[i][ind] = tmp
        G[ind][i] = tmp

def prim(G):
    visit = set([0])
    size = len(G)
    ans = [0]

    while len(ans) != size:
        m = float("inf")
        mind = None
        for f in visit:
            for t in range(size):
                if t in visit or G[f][t]==0:
                    continue
                if m > G[f][t]:
                    m = G[f][t]
                    mind = t
        ans.append(m)
        visit.add(mind)
    return ans


size = int(stdin.readline())
Graph = [[0]*size for _ in range(size)]
plist = []

for ind in range(size):
    p = list(map(float, stdin.readline().split()))
    plist.append(p)
    updateG(Graph, plist, ind)

for g in Graph:
    print(g)

ans = prim(Graph)
print(sum(ans))