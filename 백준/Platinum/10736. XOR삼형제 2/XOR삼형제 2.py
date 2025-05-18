from sys import stdin
from itertools import combinations

def update(deg, dir, tar):
    for dest in dir[tar]:
        deg[dest] -= 1
    deg[tar] = 0

def check(ans):
    for a in combinations(ans,2):
        if a[0] ^ a[1] in ans:
            return False
    return True

def solve(n):
    ans = list(range(1, n+1))
    deg = [0 for _ in range(129)]
    dir = {i:set() for i in range(1, n+1)}
    for i in range(1,n):
        for j in range(i+1, n+1):
            dest = i^j
            deg[i] += 1
            deg[j] += 1
            deg[dest] += 1

            dir[i].add(dest)
            dir[j].add(dest)
    
    
    while not check(ans):
        maxInd = deg.index(max(deg[1:n+1]))
        ans.remove(maxInd)
        update(deg, dir, maxInd)
    print(len(ans))
    print(*ans)

for _ in range(int(stdin.readline())):
    solve(int(stdin.readline()))