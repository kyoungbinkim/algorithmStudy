from sys import stdin
import math
import copy

def vectorMatch(veclist, start, dep, tar):
    if dep == tar:
        Sum = [0,0]
        for i in range(len(veclist)):
            Sum[0] += veclist[i][0]
            Sum[1] += veclist[i][1]
        return math.sqrt(Sum[0]**2 + Sum[1]**2)
    ans = []
    for i in range(start, len(veclist) + dep - tar + 1):
        tmp = copy.deepcopy(veclist)
        tmp[i][0] , tmp[i][1] = -tmp[i][0] , -tmp[i][1]
        ans.append(vectorMatch(tmp, i+1, dep+1, tar))
    return min(ans)


for _ in range(int(stdin.readline())):
    vecNum = int(stdin.readline())
    vecList = []
    for _ in range(vecNum):
        vecList.append(list(map(int, stdin.readline().split())))
    print(vectorMatch(vecList, 0, 0, vecNum//2))
    