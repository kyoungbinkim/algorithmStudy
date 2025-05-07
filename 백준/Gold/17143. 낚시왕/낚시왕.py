from sys import stdin
dir = [
    (-1,0),
    (1,0),
    (0,1),
    (0,-1)
]

def changeDir(d):
    return d+1 if d%2 ==0 else d-1

class FisherKing:
    def __init__(self):
        self.n, self.m, self.num = map(int, stdin.readline().split())

        self.fisher, self.ans = 0, 0

        self.mod = [self.n*2-2, self.m*2-2]
        self.posMap = {}
        for _ in range(self.num):
            r, c, speed, d, size= map(int ,stdin.readline().split())

            self.posMap[(r-1,c-1)] = (size, d-1, speed % self.mod[(d-1)//2])
    
        for _ in range(self.m):
            self.removeShark()
            self.moveShark()
        print(self.ans)

    def removeShark(self):
        c = self.fisher

        for r in range(self.n):
            if self.posMap.get((r,c)) != None:
                self.ans += self.posMap[(r,c)][0]
                
                self.posMap[(r,c)] = None
                break
        self.fisher += 1


    def moveShark(self):
        newPosMap = {}

        for k in self.posMap.keys():
            if self.posMap[k] == None:
                continue
            
            pos = k
            
            size, d, speed = self.posMap[pos]

            dr,dc = pos[0] + speed * dir[d][0], pos[1] + speed * dir[d][1]
            while not (0 <= dr < self.n and 0<=dc <self.m):
                if dr<0 or dc <0:
                    dr = -dr if dr <0 else dr
                    dc = -dc if dc <0 else dc
                    d = changeDir(d)

                elif dr>= self.n or dc >= self.m:
                    dr = self.mod[0] - dr if dr >= self.n else dr
                    dc = self.mod[1] - dc if dc >= self.m else dc
                    d = changeDir(d)
            if newPosMap.get((dr,dc)) == None:
                newPosMap[(dr,dc)] = []
            newPosMap[(dr,dc)].append((size, d, speed))
        

        for k in newPosMap:
            if len(newPosMap[k]) == 1:
                newPosMap[k] = newPosMap[k][0]
            else:
                newPosMap[k].sort()
                newPosMap[k] = newPosMap[k][-1]
        
        self.posMap = newPosMap

FisherKing()