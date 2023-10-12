from sys import stdin
from random import randrange


n = int(stdin.readline())

guilty = list(map(int, stdin.readline().split()))

r = [list(map(int, stdin.readline().split())) for _ in range(n)]

mafia = int(stdin.readline())


# n = 16

# guilty = [randrange(300, 800,1) for _ in range(16)]

# r = [[randrange(-25, 25, 1) for _ in range(16)] for _ in range(16)]

# mafia = randrange(0, 15)



isDead = set([])

# guilty, dead, kill index
def night(g, d, idx):
    newG = g.copy()

    newG[idx] = -1

    for i in range(n):
        newG[i] += r[idx][i] if newG[i] > 0 else 0
    
    return (newG, d.union(set([idx])))

def noon(g):
    idx = g.index(max(g))

    g[idx] = -1
    return (g, idx)


# print(r, guilty)

def DFS(g, d, cnt):
    if mafia in d:
        return cnt

    ans = -1
    for i in range(n):
        
        if ans >= n//2:
            break

        if i in d or i == mafia:
            continue
        newG, newDead = night(g, d, i)

        if len(newDead) == n-1:
            ans = max(ans , cnt)
            return cnt+1

        newG, idx = noon(newG)
        # print("noon : ", newG , idx, cnt)
        # print(newDead, newDead.union(set([idx])))
        ans = max(DFS(newG, newDead.union(set([idx])), cnt+1), ans)
        # input("ans : {}".format(ans))
    return ans

if n%2 == 1:
    newG, i = noon(guilty)
    isDead.add(i)
    guilty = newG

print(DFS(guilty, isDead, 0))

