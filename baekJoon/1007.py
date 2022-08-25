from sys import stdin
import math        

def innerProduct(v1,v2):
    return v1[0]*v2[0] + v1[1]*v2[1]

def subVector(v1,v2):
    return [v1[0]-v2[0], v1[1]-v2[1]]

def addVector(v1,v2):
    return [v1[0]+v2[0], v1[1]+v2[1]]

reandline = stdin.readline
for _ in range(int(reandline())):
    ans = float("inf")
    plist = []
    pSize = int(reandline())

    for _ in range(pSize):
        p = list(map(int, reandline().split()))
        plist.append(p)
    
    ret = plist[0]
    del plist[0]
    for v in plist:
        if innerProduct(ret, v) > 0:
            ret = subVector(ret, v)
        else:
            ret = addVector(ret, v)
    
    print(math.sqrt(ret[0]**2 + ret[1]**2))
    