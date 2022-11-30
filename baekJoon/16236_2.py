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

    
    def BFS(self):
        visit = set([])
        queue = []
        visit.add(str(self.loc))
        queue.append(self.loc+[0])
        go = [[-1,0], [0,-1], [0,1],[1,0]]
        
        candiate = []
        while len(queue) != 0:
            tmp = queue[0]
            del queue[0]

            if 0 < self.arr[tmp[0]][tmp[1]] < self.size:
                if len(candiate) ==0:
                    candiate.append(tmp)
                else:
                    if candiate[0][2] == tmp[2]:
                        candiate.append(tmp)
                    elif candiate[0][2] > tmp[2]:
                        break
                    
            for g in go:
                x,y = g[0] + tmp[0] , g[1]+tmp[1]
                if x<0 or x>=self.n or y<0 or y>=self.n:
                    continue
                if self.arr[x][y] > self.size or str([x,y]) in visit:
                    continue
                # print(queue, visit)
                queue.append([x,y]+[tmp[2]+1])
                visit.add(str([x,y]))

        return self.selectInd(candiate)
    

    def selectInd(self, candidate):
        # print(candidate)
        if len(candidate) == 0:
            return [-1,-1,0]
        ans = candidate[0]
        for i in range(1, len(candidate)):
            if ans[0] > candidate[i][0]:
                ans = candidate[i]
            elif ans[0] == candidate[i][0] and ans[1] > candidate[i][1]:
                ans = candidate[i]
        return ans

    def statusPrint(self):
        for a in self.arr:
            print(a)
        print("loc  : ", self.loc)
        print("size : ", self.size)
        print("clock: ", self.clock,"\n")

    def run(self):
        # self.statusPrint()
        while self.canEat():
            targetLoc = self.BFS()
            if targetLoc[0] == -1:
                break
            myLoc = self.loc
            # print(myLoc, targetLoc)
            self.clock += targetLoc[2]
            if self.cnt == self.size-1:
                self.size += 1
                self.cnt =0
            else:
                self.cnt += 1
            self.arr[myLoc[0]][myLoc[1]] = 0
            self.arr[targetLoc[0]][targetLoc[1]] = 9

            self.loc = targetLoc[:2]            
            
        return self.clock


if __name__ == "__main__":

    n = int(stdin.readline())
    arr= []
    for _ in range(n):
        arr.append(list(map(int, stdin.readline().split())))
        
    bs = babyShark(n,arr)
    print(bs.run())