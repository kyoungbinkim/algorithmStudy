import sys

readl = sys.stdin.readline
maxVal, auctionNum = map(int, readl().split())
auctionDict = {}
for _ in range(auctionNum):
    tmp = readl().split()
    name, price = tmp[0], int(tmp[1])
    if auctionDict.get(price) == None:
        auctionDict.update({price:[name]})
    else:
        auctionDict[price].append(name)

flag =False
for p in range(1, maxVal+1):
    tmp = auctionDict.get(p)
    if tmp == None:
        continue
    elif len(tmp) == 1:
        print(tmp[0],p)
        flag = True
        break
    minP = p

if not flag:
     
    for p in range(1, maxVal+1):
        tmp = auctionDict.get(p)
        
        if tmp == None:
            continue
        
        if len(tmp) < len(auctionDict.get(minP)):
            minP = p
    print(auctionDict.get(minP)[0], minP)