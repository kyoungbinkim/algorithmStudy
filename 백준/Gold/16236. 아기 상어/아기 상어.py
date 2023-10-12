from sys import stdin
from collections import deque

dir = [ (-1, 0), (0, -1), (0, 1), (1, 0) ]

class BabyShark:
    def __init__(self):
        self.babySize = 2
        self.eatNum, self.ans = 0, 0
    
        self.n = int(stdin.readline())
        self.b = []
        self.visit = set()
        for i in range(self.n):
            self.b.append(list(map(int, stdin.readline().split())))
            for j in range(self.n):
                if self.b[i][j] == 9:
                    self.babyPos = (i,j)
        
        # print(self.babyPos)
        # for bb in self.b:
        #     print(bb)
        
        self.run()

    def run(self):
        
        while self.getCloseShark():
            self.visit = set([self.babyPos])
            # print(self.babyPos, self.babySize, self.ans)
            # for bb in self.b:
            #     print(bb)
            # print()
            
        print(self.ans)
    
    def getCloseShark(self):
        visit= set([self.babyPos])
        que = [(self.babyPos)]
        cnt, findFish = 0, False

        newque = []
        while len(que):
            for d in dir:
                for p in que:
                    dr, dc = p[0] + d[0], p[1] + d[1]

                    if dr < 0 or dr>= self.n or dc<0 or dc>=self.n or (dr,dc) in visit:
                        continue

                    if self.b[dr][dc] > self.babySize:
                        continue

                    newque.append((dr,dc))
                    visit.add((dr,dc))

                    # if 0 < self.b[dr][dc] < self.babySize:
                    #     self.eatNum += 1

                    #     if self.eatNum == self.babySize:
                    #         self.babySize += 1
                    #         self.eatNum = 0
                        
                    #     self.b[self.babyPos[0]][self.babyPos[1]] = 0
                    #     self.babyPos = (dr,dc)
                    #     self.b[self.babyPos[0]][self.babyPos[1]] = float("inf")
                    #     findFish = True
                    #     break
            newque.sort()
            # print(newque)
            for (dr,dc) in newque:
                if 0 < self.b[dr][dc] < self.babySize:
                    self.eatNum += 1

                    if self.eatNum == self.babySize:
                        self.babySize += 1
                        self.eatNum = 0
                    self.b[self.babyPos[0]][self.babyPos[1]] = 0
                    self.babyPos = (dr,dc)
                    self.b[self.babyPos[0]][self.babyPos[1]] = float("inf")
                    findFish = True
                    break
            if findFish:
                self.ans += (cnt + 1)
                break
            cnt += 1
            que = newque.copy()
            newque = []

        return findFish


    def getClosestShart(self, pos, cnt):
        r,c = pos
        if 0 < self.b[r][c] < self.babySize:
            self.eatNum += 1
            if self.eatNum == self.babySize:
                self.eatNum = 0
                self.babySize += 1
            
            self.b[self.babyPos[0]][self.babyPos[1]] = 0 
            self.babyPos = pos
            self.b[self.babyPos[0]][self.babyPos[1]] = 9
            self.ans += cnt
            return True
        
        for d in dir:
            dr, dc = r+d[0], c+d[1]

            if dr < 0 or dr >= self.n or dc < 0 or dc >= self.n or (dr, dc) in self.visit:
                continue
            
            if self.b[dr][dc] > self.babySize:
                continue
            
            self.visit.add((dr,dc))
            tmp = self.getClosestShart((dr, dc), cnt+1)
            if tmp:
                return tmp
        
        return False



bs = BabyShark()
        