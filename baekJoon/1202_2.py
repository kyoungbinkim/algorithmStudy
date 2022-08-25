from sys import stdin
readline = stdin.readline

class heap:
    def __init__(self, items) -> None:
        self.queue = items.copy()

        for i in range(len(items)//2 , -1, -1):
            self.heapify(i)
    
    def insert(self, n):
        self.queue.append(n)
        ind = len(self.queue)-1

        while ind > 0:
            pInd = self.parent(ind)
            if pInd >= 0 and self.queue[pInd][1] < self.queue[ind][1]:
                self.swap(ind , pInd)
                ind = pInd
            else:
                break
    
    def pop(self):
        lastInd = len(self.queue)-1
        if lastInd < 0:
            return -1
        self.swap(lastInd, 0)
        mval = self.queue.pop()
        self.heapify(0)

        return mval

    def heapify(self, ind):
        lind = self.leftchild(ind)
        rind = self.rightchild(ind)
        maxind = ind

        for i in [lind, rind]:
            if self.getVal(maxind) < self.getVal(i):
                maxind = i
        
        if maxind != ind:
            self.swap(ind, maxind)
            self.heapify(maxind)


    def swap(self, ind1, ind2):
        self.queue[ind1], self.queue[ind2] = self.queue[ind2], self.queue[ind1]

    def check(self,ind):
        if ind < 0 or ind >= len(self.queue):
            return -1
        return ind

    def parent(self,ind):
        return self.check((ind-1) // 2)

    def leftchild(self, ind):
        return self.check(ind*2 + 1)

    def rightchild(self, ind):
        return self.check(ind*2 + 2)

    def getVal(self, ind):
        if self.check(ind) != -1:
            return self.queue[ind][1]
        return -1

def binarySearch(l, val):
    maxV = max(l)
    if maxV < val:
        return False
    if l[0] >= val:
        ans = l[0]
        del l[0]
        return True
    
    low, high = 0, len(l)-1
    
    while low <= high:
        mid = (low+high)//2

        if l[mid]>= val >l[mid-1]:
            ans = l[mid]
            del l[mid]
            return True
        elif l[mid] > val:
            high = mid -1
        else:
            low = mid + 1
    return False
        


infoNum, bagNum = map(int, readline().split())
items = []
Clist = []

for _ in range(infoNum):
    items.append(list(map(int, readline().split())))
myHeap = heap(items)

for _ in range(bagNum):
    Clist.append(int(readline()))
Clist.sort()

Ans = 0
while len(Clist) > 0:
    m, v = myHeap.pop() 
    flag = binarySearch(Clist, m)
    if flag:
        Ans += v
print(Ans)
