from sys import stdin

n = int(stdin.readline())

mat = [list(map(int, stdin.readline().split())) for _ in range(n)]

def dfs(pos, visit):
    

    for (idx, flag) in enumerate(mat[pos]):
        if flag and idx not in visit:
            visit.add(idx)
            visit = visit.union(dfs(idx, visit))
    
    return visit

for i in range(n):
    for j in dfs(i, set([])):
        mat[i][j] = 1

for line in mat:
    for c in line:
        print(c, end=' ')
    print()
