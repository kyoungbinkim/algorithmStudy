def calc4(List):
    a,b,c,d = List
    return max([(a+b)*c*d, a*(b+c)*d, a*b*(c+d), b*c*(d+a)])

def getList(arr, p1,p2):
    ret =[0,0,0,0]
    for i in range(len(arr)):
        for j in range(len(arr[0])):
            if i < p1 and j < p2:
                ret[0] += arr[i][j]
            elif i < p1 and j>= p2:
                ret[1] += arr[i][j]
            elif j>=p2:
                ret[2] += arr[i][j]
            else:
                ret[3] += arr[i][j]
    return ret

def calcRow(arr, row):
    maxValue = 0
    tmp = []
    for line in arr:
        tmp.append(sum(line))
    for i in range(1,row-1):
        for j in range(i+1, row):
            # print(tmp[:i], tmp[i:j],tmp[j:])
            a,b,c = sum(tmp[:i]), sum(tmp[i:j]), sum(tmp[j:])
            if a*b*c > maxValue:
                maxValue = a*b*c
    return maxValue

def calcCol(arr, col):
    maxValue = 0
    tmp = arr[0].copy()
    for line in arr[1:]:
        for i in range(col):
            tmp[i] += line[i]
    
    for i in range(1,col-1):
        for j in range(i+1, col):
            # print(tmp[:i], tmp[i:j],tmp[j:])
            a,b,c = sum(tmp[:i]), sum(tmp[i:j]), sum(tmp[j:])
            if a*b*c > maxValue:
                maxValue = a*b*c

    return maxValue

def calc(arr, row, col):
    maxValue = 0
    for i in range(1, row):
        for j in range(1, col):
            l = getList(arr, i, j)
            maxValue = max([maxValue, calc4(l)])
    return maxValue

            


arr = []
maxVal = 0
row,col = map(int, input().split())
for i in range(row):
    arr.append([int(x) for x in input()])


maxVal = calcRow(arr, row)
maxVal = max([maxVal, calcCol(arr, col)])

maxVal = max([maxVal, calc(arr, row, col)])
print(maxVal)




        