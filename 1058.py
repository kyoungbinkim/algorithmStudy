from sys import stdin

def isFriend(c):
    if c == 'Y':
        return 1
    else:
        return 0

def plusArr(a1, a2):
    ret = [x or y for x,y in zip(a1,a2)]
    return ret

ans = 0
friendNum = []
friendInd = []
for _ in range(int(stdin.readline())):
    string = stdin.readline()
    tmp = []
    for s in string:
        tmp.append(isFriend(s))
    friendNum.append(sum(tmp))
    friendInd.append(tmp)

friendLen = len(friendInd)
for ind in range(friendLen):
    me = friendInd[ind]
    for i in range(friendLen):
        if friendInd[ind][i] == 1:
            me = plusArr(me, friendInd[i])
    me[ind] = 0
    if ans < sum(me):
        ans = sum(me)
print(ans)

