from sys import stdin

def getVal(arr, p, size):
    if p[0] <0 or p[1] <0 or p[0]>= size or p[1]>=size:
        return 0
    return arr[p[0]][p[1]]

def partSum(arr, size, p):
    lu = {}
    ru = {}
    ans = []
    ret = 0
    for _ in range(size):
        ans.append([0]*size)
    
    for i in range(p[0]):
        for j in range(p[1]):
            ans[i][j] = getVal(arr, [p[0]-1, p[1]-1],size) - getVal(arr, [i-1,p[1]-1],size)\
                - getVal(arr, [p[0]-1, j-1],size) + getVal(arr, [i-1, j-1], size)
            
            if lu.get(ans[i][j]) == None:
                lu.update({ans[i][j] : 1})
            else:
                lu[ans[i][j]] += 1
            
    for i in range(p[0], size):
        for j in range(p[1]):
            ans[i][j] = getVal(arr, [p[0]-1, j-1],size) + getVal(arr, [i,p[1]-1],size) \
                - getVal(arr, [p[0]-1, p[1]-1],size) - getVal(arr, [i, j-1], size)
            
            if ru.get(ans[i][j]) == None:
                ru.update({ans[i][j] : 1})
            else:
                ru[ans[i][j]] += 1
    
    for i in range(p[0]):
        for j in range(p[1],size):
            ans[i][j] = getVal(arr, [p[0]-1, j],size)+ getVal(arr, [i-1,p[1]-1],size) \
                - getVal(arr, [i-1, j],size) - getVal(arr, [p[0]-1,p[1]-1],size)
            if ru.get(ans[i][j]) != None:
                ret += ru[ans[i][j]]
    
    for i in range(p[0],size):
        for j in range(p[1],size):
            ans[i][j] = getVal(arr, [i, j],size)+ getVal(arr, [p[0]-1,p[1]-1],size) \
                - getVal(arr, [p[0]-1, j],size) -  getVal(arr, [i,p[1]-1],size)
            if lu.get(ans[i][j]) != None:
                ret += lu[ans[i][j]]

    # for a in ans:
    #     print(a)
    
    return ret
    

total = 0
arrSize = int(stdin.readline())
arr = []
arrSum = []

for _ in range(arrSize):
    arr.append(list(map(int, stdin.readline().split())))
    arrSum.append([0] * arrSize)


arrSum[0] = [sum(arr[0][:i+1]) for i in range(arrSize)]
for i in range(1, arrSize):
    for j in range(arrSize):
        arrSum[i][j] += (arrSum[i-1][j] + arr[i][j])
        if j == 0:
            continue
        arrSum[i][j] += arrSum[i][j-1]
        arrSum[i][j] -= arrSum[i-1][j-1]

# for a in arrSum:
#     print(a)
# print()

for i in range(1,arrSize):
    for j in range(1, arrSize):
        # print(i,j)
        total += partSum(arrSum, arrSize, [i,j])
        # print()
print(total)