from sys import stdin

treeNum, minSize = map(int, stdin.readline().split())
treeList = list(map(int, stdin.readline().split()))
treeMap = {}
for t in treeList:
    if treeMap.get(t) == None:
        treeMap.update({t:1})
    else:
        treeMap[t]+=1
del treeList
keyList = list(treeMap.keys())
def getTreeVal(keyList, ans):
    tmp = 0
    for k in keyList:
        if k > ans:
            tmp += (k-ans) * treeMap[k]
    return tmp

high = max(keyList)
low = 0
ans = 0
while high>= low:
    mid = (low + high) //2
    tmp = getTreeVal(keyList, mid)
    # print(tmp, mid, low,high)
    if tmp == minSize:
        break
    elif tmp > minSize:
        low = mid+1
    else:
        high = mid-1

if tmp < minSize:
    mid -= 1
print(mid)


# 5 8
# 17 18 19 21 21