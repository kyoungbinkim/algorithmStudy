import copy

def Point(arr, p):
    for i in range(len(arr)):
        for j in range(len(arr)):
            if i == p[0] or j == p[1]:
                arr[i][j] = 1
                continue
            if abs(j-p[1]) == abs(i-p[0]):
                arr[i][j] = 1

def NQueen(arr,iter,size):
    k = 0
    if iter == size:
        return 1
    for i in range(size):
        if arr[iter][i] == 0:
            arrCopy = copy.deepcopy(arr)
            Point(arrCopy, [iter,i])
            k += NQueen(arrCopy, iter+1, size)
    return k

n = int(input())
arr, tmp = [], [0]*n
for _ in range(n):
    arr.append(tmp.copy())

print(NQueen(arr, 0, n))

