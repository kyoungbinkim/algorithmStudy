from sys import stdin
readline = stdin.readline

class pq:
    def __init__(self):
        self.queue = []
        self.lenq = 0
    
    def update(self, l):
        
        if self.lenq == 0:
            self.queue.append(l)
            self.lenq += 1
            return

        for i in range(0, self.lenq):
            if l[1] > self.queue[i][1]:
                self.queue.insert(i, l)
                self.lenq += 1
                return
        self.lenq += 1
        self.queue.append(l)
        
    def pop(self):
        ret = self.queue[0]
        del self.queue[0]
        self.lenq -= 1
        return ret

    def clac(self, clist):
        ans = 0

        while len(clist) != 0:
            tmp = self.pop()

            for i in range(len(clist)):
                if clist[i] >= tmp[0]:
                    ans += tmp[1]
                    del clist[i]
                    break
            if len(self.queue) == 0:
                break
        return ans

infoNum, bagNum = map(int, readline().split())
Clist = []
Pq = pq()

for _ in range(infoNum):
    Pq.update(list(map(int, readline().split())))

for _ in range(bagNum):
    Clist.append(int(readline()))
Clist.sort()

print(Pq.clac(Clist))
    
