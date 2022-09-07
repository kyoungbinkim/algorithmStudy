from sys import stdin
import sys

sys.setrecursionlimit(10**9)

class babyShark:

    def __init__(self,n, a) -> None:
        self.cnt = 0
        self.clock = 0
        self.n = n
        self.arr= a
        self.size= 2
        self.loc = None
        for i in range(n):
            for j in range(n):
                if self.arr[i][j] == 9:
                    self.loc = [i,j]
                    break
            if self.loc != None:
                break
    
    def canEat(self):        
        for i in range(self.n):
            for j in range(self.n):
                if self.arr[i][j] == 9:
                    continue
                if  0 < self.arr[i][j] < self.size:
                    return True
        return False

    def Distance(self, p1, p2,visit, l):
        if p1[0] == p2[0] and p1[1] == p2[1]:
            return l
        go = [[-1,0], [0,-1], [0,1],[1,0]]
        tmp = []
        for g in go:
            x,y = g[0] + p1[0] , g[1]+p1[1]
            if x<0 or x>=self.n or y<0 or y>=self.n:
                continue

            tmp.append(self.Distance([x,y], p2, l+1))
        if len(tmp) == 0:
            return float("inf")
        return min(tmp)

    
    def BFS(self):
        visit = set([])
        queue = []
        visit.add(str(self.loc))
        queue.append(self.loc+[0])
        go = [[-1,0], [0,-1], [0,1],[1,0]]
        while len(queue) != 0:
            tmp = queue[0]
            del queue[0]

            if 0 < self.arr[tmp[0]][tmp[1]] < self.size:
                return tmp

            for g in go:
                x,y = g[0] + tmp[0] , g[1]+tmp[1]
                if x<0 or x>=self.n or y<0 or y>=self.n:
                    continue
                if self.arr[x][y] > self.size or str([x,y]) in visit:
                    continue
                # print(queue, visit)
                queue.append([x,y]+[tmp[2]+1])
                visit.add(str([x,y]))
        return [-1, -1]


    def DFS(self, ind, visit, l):
        go = [[-1,0], [0,-1], [0,1],[1,0]]
        visit.add(str(ind))
        ans, Ansdist = None,None
        tmp = []
        for g in go:
            x,y = g[0] + ind[0] , g[1]+ind[1]
            if x<0 or x>=self.n or y<0 or y>=self.n:
                continue
            if self.arr[x][y] > self.size:
                continue
            if 0 < self.arr[x][y] < self.size:
                return [x,y], l+1
            if ans == None or ans == []:
                ans, Ansdist = self.DFS([x,y], visit, l+1)
                
                print("ans : ", ans)
            else:
                tmp, tmpdist  = self.DFS([x,y], visit, l+1)
                if tmp != [] and tmp != None:
                    print(ans, tmp, Ansdist, tmpdist)
                    if tmpdist < Ansdist:
                        ans, Ansdist= tmp, tmpdist
                    elif tmpdist == Ansdist:
                        if tmp[0] < ans[0]:
                            ans, Ansdist= tmp, tmpdist
                        elif tmp[0] == ans[0] and tmp[1] < ans[1]:
                            ans, Ansdist= tmp, tmpdist

        return ans, Ansdist


    def closestFish(self) -> list:
        closeInd = [self.n+1, self.n+1]
        closeDistance = float("inf")
        #or (self.arr[i][j] == self.size and i<closeInd[0])
        for i in range(self.n):
            for j in range(self.n):
                if (0< self.arr[i][j] < self.size):
                    # if self.loc == [0,0]:
                    #     print(abs(i-self.loc[0]) + abs(j-self.loc[1]), i ,j, closeDistance, closeInd)
                    dist = abs(i-self.loc[0]) + abs(j-self.loc[1])
                    if dist < closeDistance:
                        closeInd = [i,j]
                        closeDistance = dist
                    elif dist == closeDistance and i<= closeInd[0] and j<closeInd[1]:
                        closeInd = [i,j]
                        closeDistance = dist
        return closeInd
    
    def statusPrint(self):
        for a in self.arr:
            print(a)
        print("loc  : ", self.loc)
        print("size : ", self.size)
        print("clock: ", self.clock,"\n")

    def run(self):
        self.statusPrint()
        while self.canEat():
            # targetLoc = self.closestFish()
            # targetLoc, dist = self.DFS(self.loc, set([]), 0)
            targetLoc = self.BFS()
            myLoc = self.loc
            print(myLoc, targetLoc)
            # self.clock += (abs(targetLoc[0]-self.loc[0]) + abs(targetLoc[1]-self.loc[1]))
            self.clock += targetLoc[2]
            if self.cnt == self.size-1:
                self.size += 1
                self.cnt =0
            else:
                self.cnt += 1
            self.arr[myLoc[0]][myLoc[1]] = 0
            self.arr[targetLoc[0]][targetLoc[1]] = 9

            self.loc = targetLoc[:2]

            self.statusPrint()
            if self.size > 10:
                break
            
        return self.clock


if __name__ == "__main__":

    n = int(stdin.readline())
    arr= []
    for _ in range(n):
        arr.append(list(map(int, stdin.readline().split())))
        
    bs = babyShark(n,arr)
    print(bs.run())
            
            


        
        