from sys import stdin
rl = stdin.readline
permArr = []
def getlist(arr, dep, ret):
    for i in range(len(arr)):
        tmp = arr.copy()
        tmpret = ret.copy()
        tmpret.append(tmp[i])
        del tmp[i]
        if dep ==3:
            permArr.append(tmpret)
            return
        else:
            getlist(tmp, dep+1, tmpret)


getlist([0,1,2], 1, [])
houses = []
for _ in range(int(rl())):
    houses.append(list(map(int, rl().split())))
ans = float("inf")
for perm in permArr:
    tmp = 0
    tmp += min([houses[0][perm[0]], houses[0][perm[2]]])
    tmp += min([houses[len(houses)-1][perm[(len(houses)-1)%3]], houses[len(houses)-1][perm[(len(houses))%3]]])
    for i in range(1,len(houses)-1):
        print(i%3, perm[i%3],houses[i][perm[i%3]])
        tmp += houses[i][perm[i%3]]
    
    if tmp < ans:
        ans = tmp
        print("!!1",ans)
    print("")
print(ans)