from operator import xor


d = {"W":1, "B":0}

def diff(arr1, arr2, row,col):
    ans = 0
    for i in range(row):
        for j in range(col):
            # print(arr1[i][j], arr2[i][j], xor(arr1[i][j], arr2[i][j]))
            ans += xor(arr1[i][j], arr2[i][j])
    return ans

def getarr(arr, ind):
    ret = []
    for i in range(ind[0], ind[0]+8):
        ret.append(arr[i][ind[1]:ind[1]+8].copy())
    return ret

row,col = map(int, input().split())

ans1,ans2 = [],[]
for i in range(8):
    ans1.append([(x+i)%2 for x in range(8)])
    ans2.append([(x+i+1)%2 for x in range(8)])

arr = []
for _ in range(row):
    arr.append([d[x] for x in input()])


a =64
for i in range(row-7):
    for j in range(col-7):
        tarr = getarr(arr, [i,j])
        tmp = min([diff(tarr,ans1,8, 8), diff(tarr, ans2, 8, 8)])
        if a > tmp:
            a= tmp
print(a)

