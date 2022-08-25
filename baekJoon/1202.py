from sys import stdin
readline = stdin.readline

class priorQ:
    def __init__(self):
        self.m2v = {}
    
    def upload(self, l):
        if self.m2v.get(l[0]) == None:
            self.m2v.update({l[0]:[l[1]]})
        else:
            self.m2v[l[0]].append(l[1])
    
    def Sort(self):
        for k in self.m2v.keys():
            self.m2v[k].sort(reverse=True)
        self.keyList = list(self.m2v.keys())
        self.keyList.sort()
    
    def Pop(self, C):
        maxInd = self.keyList[0]
        ans = 0
        for k in self.keyList:
            if k>C:
                break
            if self.m2v[k][0] >= self.m2v[maxInd][0]:
                maxInd = k
                ans = self.m2v[maxInd][0]
        if ans != 0:
            del self.m2v[maxInd][0]
        if len(self.m2v[maxInd]) == 0:
            del self.m2v[maxInd]
            self.keyList.remove(maxInd)
        return ans

infoNum, bagNum = map(int, readline().split())
Clist = []
pq = priorQ()
for _ in range(infoNum):
    pq.upload(list(map(int, readline().split())))
pq.Sort()
# print(pq.keyList, pq.m2v)

for _ in range(bagNum):
    Clist.append(int(readline()))
Clist.sort()
# print(Clist)

ans = 0
for c in Clist:
    ans += pq.Pop(c)
    # print(pq.keyList, pqs.m2v)
print(ans)



# 10 5
# 5 20
# 6 33
# 7 44
# 7 54
# 7 22
# 1 19
# 2 21
# 10 100
# 5 21
# 6 17
# 5 
# 6
# 7
# 5
# 10