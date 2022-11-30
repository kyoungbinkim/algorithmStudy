from sys import stdin

direction = {0:[-1,0] , 1:[0,1], 2:[1,0], 3:[0,-1]}

class robot:
    def __init__(self, start, map, dir):
        self.ind = start
        self.map = map
        self.dir = dir
        self.h, self.w = len(self.map), len(self.map[0])
    
    def turnLeft(self):
        self.dir = (self.dir - 1) + 4 if (self.dir - 1) < 0 else  (self.dir - 1)
    
    def Go(self):
        self.ind = [self.ind[0]+direction[self.dir][0], self.ind[1]+direction[self.dir][1]]
    
    def GoBack(self):
        y_, x_ = self.ind[0]-direction[self.dir][0], self.ind[1]-direction[self.dir][1]
        if y_==0 or y_ ==self.h-1:
            return False
        if x_==0 or x_==self.w-1:
            return False
        if self.map[y_][x_] == 1:
            return False
        self.ind = [y_, x_]
        return True
    
    def canGo(self):
        tmpDir =  (self.dir - 1) + 4 if (self.dir - 1) < 0 else  (self.dir - 1)
        y_, x_ = self.ind[0]+direction[tmpDir][0], self.ind[1]+direction[tmpDir][1]
        if y_<0 or y_ >=self.h:
            return False
        if x_<0 or x_>=self.w:
            return False
        if self.map[y_][x_] != 0:
            return False
        return True
    
    def run(self):
        ans = 0
        while True:
            
            flag = False
            if self.map[self.ind[0]][self.ind[1]] == 0:
                ans += 1
            self.map[self.ind[0]][self.ind[1]] = 2
            # self.printMap()
            for i in range(4):
                if self.canGo():
                    self.turnLeft()
                    self.Go()
                    flag = True
                    break
                self.turnLeft()
            if flag:
                continue
            if self.GoBack():
                continue
            break
        return ans
    
    def printMap(self):
        print(self.dir, direction[self.dir])
        for a in self.map:
            print(a)
        print()

    

arr = []
hi, wi = map(int, stdin.readline().split())
x,y,d = map(int,stdin.readline().split())
for i in range(hi):
    
    arr.append(list(map(int, stdin.readline().split())))
robo = robot([x,y], arr, d)
print(robo.run())

