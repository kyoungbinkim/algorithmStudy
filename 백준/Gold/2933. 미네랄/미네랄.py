from sys import stdin
from collections import deque

char2num = {
    '.' : 0, 'x': 1
}

dir = [
    (1,0), (-1,0), (0,1), (0,-1)
]

class Mineral:
    def __init__(self):
        self.mineDir = 1
        self.n,self.m = map(int, stdin.readline().split())

        self.board = [[char2num[c] for c in stdin.readline().removesuffix('\n')] for _ in range(self.n)]
        self.board = self.board[::-1]

        self.mineral = set()

        for i in range(self.n):
            for j in range(self.m):
                if self.board[i][j]:
                    self.mineral.add((i,j))

        self.mineNum = int(stdin.readline())
        self.mineList = list(map(lambda x : int(x)-1, stdin.readline().split()))

        for line in self.mineList:
            self.mine(line)
            self.splitCluster()
            
            # print(line)
            # for b in self.board:
            #     print(b)
            # print()
        
        for line in self.board[::-1]:
            tmp = ''
            for c in line:
                tmp += '.' if c == 0 else 'x'
            print(tmp)


    def mine(self, line):

        for i in range(int(self.mineDir == -1), self.m + int(self.mineDir == -1)):
            if self.board[line][self.mineDir * i]:
                self.board[line][self.mineDir * i] = 0

                self.mineral.remove((line,(self.m + self.mineDir * i) % self.m))

                break
        self.mineDir *= -1

    def splitCluster(self):
        start = None
        visit = set()
        clusters = []

        for i in range(self.n):
            for j in range(self.m):
                if self.board[i][j] and (i,j) not in visit:
                    start = (i,j)
                    clusters.append(set([start]))
                    que = deque([start])

                    while len(que):
                        pos = que.popleft()

                        for d in dir:
                            move = (pos[0] + d[0], pos[1] + d[1])

                            if move in self.mineral and move not in visit:
                                que.append(move)
                                visit.add(move)
                                clusters[-1].add(move)
        # print(clusters)
        self.moveCluster(clusters)

    def moveCluster(self, clusters):
        remain = self.mineral.difference(clusters[-1])
        for (r,c) in clusters[-1]:
            self.board[r][c] = 0

        while 1:
            moved = set()

            for (r,c) in clusters[-1]:

                dr, dc = r-1, c

                if dr < 0 or (dr,dc) in remain:
                    break
                
                moved.add((dr,dc))
            
            if len(clusters[-1]) == len(moved):
                clusters[-1] = moved
            else:
                break
        
        
        for (r,c) in clusters[-1]:
            self.board[r][c] = 1
        
        self.mineral = clusters[-1].union(remain)


Mineral()