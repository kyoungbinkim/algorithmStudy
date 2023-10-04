from sys import stdin

r,c,k = map(int ,stdin.readline().split())
mat = [list(map(int, stdin.readline().split())) for _ in range(3)]

n,m = 3, 3

def R(mat):
    newMat = []
    for l in mat:
        tmp = {}
        
        for num in l:
            if num == 0:
                continue
            if tmp.get(num) == None:
                tmp[num] = 0
            tmp[num] += 1
        newLine = []
        for k in tmp.keys():
            newLine.append([k, tmp[k]])
        newLine.sort(key=lambda x: (x[1], x[0]))
        s = []
        for nl in newLine:
            s += nl
        newMat.append(s)
    
    maxLen = max([len(x) for x in newMat])
    for nl in newMat:
        nl += [0 for _ in range(maxLen - len(nl))]
    return newMat

def C(mat):
    newMat = []

    for l in [[m[i] for m in mat] for i in range(len(mat[0]))]:
    
        tmp = {}
        
        for num in l:
            if num == 0:
                continue
            if tmp.get(num) == None:
                tmp[num] = 0
            tmp[num] += 1
        newLine = []
        for k in tmp.keys():
            newLine.append([k, tmp[k]])
        newLine.sort(key=lambda x: (x[1], x[0]))
        s = []
        for nl in newLine:
            s += nl
        newMat.append(s)
    maxLen = max([len(x) for x in newMat])
    for nl in newMat:
        nl += [0 for _ in range(maxLen - len(nl))]

    newnewMat = []

    for i in range(maxLen):
        newnewMat.append([x[i] for x in newMat])
    return newnewMat

for tic in range(101):
    if len(mat) >= r and len(mat[0]) >= c and mat[r-1][c-1] == k:
        print(tic)
        exit(0)
    if len(mat) >= len(mat[0]):
        mat = R(mat)
    else:
        mat = C(mat)
    
    
print(-1)


