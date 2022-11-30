from sys import stdin

def update(ml):
    maxind = 0
    for i in range(1, len(ml)-1):
        if ml[maxind][1] < ml[i][1]:
            maxind = i
    
    ret = ml[maxind][0]*ml[maxind][1] * ml[maxind+1][1]
    tmp = [ml[maxind][0], ml[maxind+1][1]]
    del ml[maxind]
    del ml[maxind]
    ml.insert(maxind, tmp)
    return ret


lenL = []
matList,matArr,size = [], [], int(stdin.readline())
for i in range(size):
    matList.append(list(map(int, stdin.readline().split())))
    matArr.append([0]*size)
    lenL.append(matList[i][0])
lenL.append(matList[size-1][1])

ans = 0
print(matList)
while len(matList) >1 :
    ans += update(matList)
    
    print(ans,matList)


# 4
# 5 3
# 3 2
# 2 6
# 6 3