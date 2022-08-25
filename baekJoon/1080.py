from sys import stdin
rl = stdin.readline

def printMat(mat):
    for s in mat:
        print(s)
    
def getMatrix(row):
    mat = []
    for _ in range(row):
        mat.append([int(s) for s in rl().split()[0]])
    return mat

def updateMat(mat, ind):
    if sum(mat[ind[0]][ind[1]:ind[1]+3]) == 3:
        for i in range(3):
            for j in range(3):
                mat[ind[0]+i][ind[1]+j] = int(not mat[ind[0]+i][ind[1]+j])
        return True
    elif mat[ind[0]][ind[1]] + mat[ind[0]+1][ind[1]] + mat[ind[0]+2][ind[1]] == 3:
        for i in range(3):
            for j in range(3):
                mat[ind[0]+i][ind[1]+j] = int(not mat[ind[0]+i][ind[1]+j])
        return True
    return False
row,col = map(int, rl().split())
matrix1, matrix2= getMatrix(row), getMatrix(row)
mat = []

for i in range(row):
    mat.append([])
    for j in range(col):
        if matrix1[i][j] != matrix2[i][j]:
            mat[i].append(1)
        else:
            mat[i].append(0)
# printMat(mat)
ans = 0
for i in range(row-2):
    for j in range(col-2):
        ans += updateMat(mat, [i,j])
        # printMat(mat)

if sum([sum(s) for s in mat]) >0 :
    print(-1)
else:
    print(ans)