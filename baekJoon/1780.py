from sys import stdin
global ans
ans = [0,0,0]

def isTrue(Arr, ind, s):
    global ans
    Ans = Arr[ind[0]][ind[1]]
    for i in range(ind[0],ind[0]+s):
        for j in range(ind[1], ind[1]+s):
            if Arr[i][j] != Ans:
                return False
    ans[Ans+1] += 1
    return True

def printArr(Arr):
    for a in Arr:
        print(a)

def copyArr(arr, ind, size):
    tmp = []
    for i in range(size):
        tmp.append([])
        for j in range(size):
            tmp[i].append(arr[ind[0]+i][ind[1]+j])
    return tmp

def update(Arr, ind, size):
    
    if isTrue(Arr, ind, size):
        return
    s = len(Arr) // 3
    for i in range(3):
        for j in range(3):
            update(Arr, [ind[0]+ i*s, ind[1]+j*s], s)
    
    
arr = []
arrSize = int(stdin.readline())
for i in range(arrSize):
    arr.append(list(map(int, stdin.readline().split())))

update(arr, [0,0], len(arr))
for a in ans:
    print(a)