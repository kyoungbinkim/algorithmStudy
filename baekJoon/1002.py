import math

def getDistance(x1,y1,x2,y2):
    return math.sqrt((x1-x2)**2 + (y1- y2)**2)

for _ in range(int(input())):
    tmp = []
    for s in input().split():
        tmp.append(int(s))
    x1,y1,r1,x2,y2,r2 = tmp
    if x1 == x2 and y1 == y2 and r1 == r2:
        print(-1)
        continue
    elif x1 == x2 and y1 == y2:
        print(0)
        continue

    dis = getDistance(x1,y1,x2,y2)
    print(x1,y1,x2,y2, dis)
    if max([dis, r1, r2]) == dis:

        if dis == r1+r2:
            print(1)
        elif dis > r1+r2:
            print(0)
        else:
            print(2)
    else:
        if dis + r1 == r2 or dis + r2 == r1:
            print(1)
        elif sum([dis, r1, r2])-max([dis, r1, r2]) > max([dis, r1, r2]):
            print(2)
        else:
            print(0)
    
