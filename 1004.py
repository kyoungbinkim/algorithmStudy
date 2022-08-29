import math

def string2intArr(arr):
    tmp = []
    for a in arr:
        tmp.append(int(a))
    return tmp

def getDistance(p1, p2):
    return math.sqrt((p1[0]-p2[0])**2 + (p1[1]-p2[1])**2)

def isInCircle(start, end, circle):
    radius = circle[2]
    sDis = getDistance(start,circle[:2])
    eDis = getDistance(end, circle[:2])
    if sDis < radius and eDis < radius:
        return False
    elif sDis > radius and eDis > radius:
        return False
    else:
        return True

for _ in range(int(input())):
    ans = 0
    tmp = string2intArr(input().split())
    startPoint, endPoint = [tmp[0],tmp[1]], [tmp[2], tmp[3]]
    for _ in range(int(input())):
        ans += int(isInCircle(startPoint, endPoint, string2intArr(input().split())))
    print(ans)