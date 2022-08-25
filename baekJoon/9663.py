global ans
ans = 0

def check(l):
    j = len(l) -1
    for i in range(len(l)-1):
        if j-i == abs(l[i]-l[j]):
            return False
    return True

def check2(l, num):
    for i in range(len(l)):
        if len(l) - i == abs(num - l[i]):
            return False
    return True

    

def NQueen(arr, result):
    global ans
    if len(arr) == 0:
        ans += 1
        return
    for i in range(len(arr)):

        if check2(result, arr[i]):
            arrCopy = arr.copy()
            tmp = result.copy()
            tmp.append(arrCopy[i])
            del arrCopy[i]
            NQueen(arrCopy, tmp)

        # arrCopy = arr.copy()
        # tmp = result.copy()
        # tmp.append(arrCopy[i])
        # if check(tmp):
        #     del arrCopy[i]
        #     NQueen(arrCopy, tmp)

ansList=[]
size = int(input())
arr = list(range(size))
NQueen(arr, [])
for i in range(1,size+1):
    ans = 0
    arr = list(range(i))
    NQueen(arr,[])
    ansList.append(ans)
print(ans,ansList)