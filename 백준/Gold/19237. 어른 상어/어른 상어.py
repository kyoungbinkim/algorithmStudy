from sys import stdin
from collections import deque

dir = [
    (-1,0), (1,0), (0,-1), (0,1)
]


class AdultShark:
    def __init__(self):
        self.n, self.m, self.k = map(int, stdin.readline().split())
        self.board, self.dList = [], [[]]

        self.pos = [ (-1, -1) for _ in range(self.m+1) ]

        for i in range(self.n):
            tmp = list(map(int, stdin.readline().split()))
            self.board.append(tmp)
            for j in range(self.n):
                if tmp[j] > 0:
                    self.pos[tmp[j]] = (i,j)  
            

        self.d = [-1] + list(map(lambda x: int(x)-1, stdin.readline().split()))
        self.smell = [None] + [deque([p]) for p in self.pos[1:] ]
        for i in range(1, 1 + self.m):
            self.dList.append([])
            for _ in range(4):
                self.dList[i].append(list(map(lambda x: int(x)-1, stdin.readline().split())))
        self.run()

    def run(self):
        for ans in range(1, 1001):
            for idx in range(1, self.m+1):
                self.moveShark(idx)
            
            if self.eatShark():
                print(ans)
                return
        
        print(-1)
            


    def moveShark(self, idx):
        p = self.pos[idx]

        if p == (-1, -1):
            return
        
        d = self.d[idx]
        dmap = self.dList[idx][d]

        second = None

        for i in range(4):
            dr = p[0] + dir[dmap[i]][0]
            dc = p[1] + dir[dmap[i]][1]

            if dr < 0 or dc < 0 or dr >=self.n or dc >= self.n:
                continue

            if self.board[dr][dc] == idx and second == None:
                second = ((dr,dc), dmap[i])
                continue
            elif self.board[dr][dc] > 0:
                continue

            self.pos[idx] = (dr, dc)
            self.d[idx] = dmap[i]
            return
        
        self.pos[idx] = second[0]
        self.d[idx] = second[1]
    
    def eatShark(self):

        for ((r,c), idx) in zip(self.pos[1:], range(1, self.m+1)):
            if (r,c) == (-1, -1) :
                continue
            if self.board[r][c] > 0  and self.board[r][c] < idx:
                self.pos[idx] = (-1, -1)
                continue
            self.board[r][c] = idx
        
        cnt = 0
        FLAG = len(self.smell[1]) == self.k
        for i in range(1, self.m+1):
            self.smell[i].append(self.pos[i])
            cnt += 1 if self.pos[i] != (-1, -1) else 0
            if FLAG:
                (r,c) = self.smell[i].popleft()
                if r>=0 and (r,c) not in self.smell[i]:
                    self.board[r][c] = 0
        
        return cnt == 1


AdultShark()