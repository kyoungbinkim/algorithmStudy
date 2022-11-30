from sys import stdin

tar = int(stdin.readline())

asize = int(stdin.readline())
a = list(map(int, stdin.readline().split()))
aSum = [0]
adict = {}
for i in range(asize):
    aSum.append(aSum[i] + a[i])

for l in range(1, asize+1):
    for ind in range(asize + 1 - l):
        tmp = aSum[ind+l] - aSum[ind]
        if adict.get(tmp) == None:
            adict.update({tmp:1})
        else:
            adict[tmp] += 1
    
del a
del aSum

bsize = int(stdin.readline())
b = list(map(int, stdin.readline().split())) 
bSum = [0]
bdict = {}
for i in range(bsize):
    bSum.append(bSum[i] + b[i])

for l in range(1, bsize+1):
    for ind in range(bsize + 1 - l):
        tmp = bSum[ind+l] - bSum[ind]
        if bdict.get(tmp) == None:
            bdict.update({tmp:1})
        else:
            bdict[tmp] += 1

del b
del bSum

if len(adict) < len(bdict):
    s,b = adict, bdict
else:
    s,b = bdict, adict

ans = 0
for k in s.keys():
    if b.get(tar-k) != None:
        ans += s[k] * b[tar-k]
print(ans)
