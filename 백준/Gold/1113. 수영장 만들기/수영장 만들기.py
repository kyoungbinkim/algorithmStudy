from sys import stdin
from collections import deque

dir = [ (0,1), (0,-1), (1,0), (-1, 0) ]

class MakePool:
    def __init__(self):
        self.ans = 0
        self.n,self.m = map(int, stdin.readline().split())

        self.board = [[int(c) for c in stdin.readline().removesuffix('\n')] for _ in range(self.n)]

        for th in range(1, 10):
            self.log = set()
            for i in range(self.n):
                for j in range(self.m):
                    if self.board[i][j] == th and (i,j) not in self.log:
                        self.fillPool((i,j))
            
            # for b in self.board:
            #     print(b)
            # print()
        print(self.ans)
    
    def fillPool(self, start):
        th = self.board[start[0]][start[1]]

        visit, update = set([start]), set([start])
        que = deque([start])

        while len(que):
            pos = que.popleft()

            for d in dir:
                dr,dc = pos[0] + d[0], pos[1] + d[1]

                if dr < 0 or dc < 0 or dr >=self.n or dc >= self.m:
                    return

                if (dr,dc) in visit:
                    continue

                if self.board[dr][dc] < th:
                    return
                elif self.board[dr][dc] == th:
                    self.log.add((dr,dc))
                    update.add((dr,dc))
                    que.append((dr,dc))
                visit.add((dr,dc))
                
        # print(update)
        for (r,c) in update:
            self.board[r][c] += 1
        self.ans += len(update)

MakePool()

