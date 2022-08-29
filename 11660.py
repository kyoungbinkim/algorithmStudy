from sys import stdin
rl = stdin.readline

def updateArr(arr):
    for i in range(len(arr)):
        for j in range(len(arr)):
            if i>0:
                arr[i][j] += arr[i-1][j]
            if j>0:
                arr[i][j] += arr[i][j-1]
            if i >0 and j >0:
                arr[i][j] -= arr[i-1][j-1]

def arrSum(arr, p):
    x1,y1,x2,y2 = p
    ret = arr[x2-1][y2-1]

    if x1 > 1:
        ret -= arr[x1-2][y2-1]
    if y1 >1 :
        ret -= arr[x2-1][y1-2]
    
    if x1 > 1 and y1 > 1:
        ret += arr[x1-2][y1-2]
    
    return ret

arrSize, pSize = map(int, rl().split())
arr = []
for _ in range(arrSize):
    arr.append(list(map(int, rl().split())))

updateArr(arr)

for _ in range(pSize):
    print(arrSum(arr, list(map(int, rl().split()))))
    