from sys import stdin
from collections import deque

fishMove = [
    (0,-1), (-1, -1), (-1,0), (-1, 1), (0, 1), (1, 1), (1,0), (1,-1)
]

sharkMove = [
    (-1,0), (0,-1), (1,0),(0,1)
]

class MagicShark:
    def __init__(self):
        self.m, self.s = map(int, stdin.readline().split())

        self.board = [[[0 for _ in range(8)] for _ in range(4)] for _ in range(4)]

        self.smell = [[0 for _ in range(4)] for _ in range(4)]
        self.smellLog = deque()
        
        self.iter = None

        for _ in range(self.m):
            r,c, d = map(lambda x: int(x)-1, stdin.readline().split())

            self.board[r][c][d] += 1
        
        self.shark = tuple([int(x) -1 for x in stdin.readline().split()])

        self.run()

    def run(self):

        for self.iter in range(self.s):
            after = self.moveFishs()
            ans, log = self.moveShark(self.shark, [self.shark], 0, after)
            self.shark = log[-1]
            self.updateSmell(log, after)

            for (r,c) in log[1:]:
                after[r][c] = [0 for _ in range(8)]
            
            self.board = [[[self.board[i][j][d] + after[i][j][d] for d in range(8)] for j in range(4)] for i in range(4)]

        cnt = 0
        for i in range(4):
            for j in range(4):
                cnt += sum(self.board[i][j])
        print(cnt)

    def moveFishs(self):
        after = [[[0 for _ in range(8)] for _ in range(4)] for _ in range(4)]

        for i in range(4):
            for j in range(4):
                for d in range(7, -1, -1):
                    if self.board[i][j][d] > 0:
                        for m in range(0, 9):
                            dr,dc = i+fishMove[d - m][0] , j +fishMove[d - m][1]

                            if 0<= dr <4 and 0<= dc <4 and self.smell[dr][dc] == 0 and (dr,dc) != self.shark:
                                break
                        if m == 8:
                            after[i][j][d] += self.board[i][j][d]
                            continue
                        after[dr][dc][d-m] += self.board[i][j][d]

        return after
                            
    def moveShark(self, pos, log, score, b):
        if len(log) == 4:
            return (score, log)
        
        ans, ansLog = -1, -1
        for d in sharkMove:
            dr,dc = pos[0] + d[0], pos[1] + d[1]

            if dr<0 or dc <0 or dr >=4 or dc >= 4:
                continue

            if (dr,dc) not in set(log[1:]):
                newAns, newLog = self.moveShark((dr, dc), log + [(dr,dc)], score + sum(b[dr][dc]), b)
            else:
                newAns, newLog = self.moveShark((dr, dc), log + [(dr,dc)], score, b)
            
            if newAns > ans:
                ans, ansLog = newAns, newLog
        
        return(ans, ansLog)

    def updateSmell(self, log, b):
        for (r,c) in log[1:]:
            if sum(b[r][c]):
                self.smellLog.append(((r,c), self.iter))
                self.smell[r][c] = 1
        
        while len(self.smellLog) and self.iter - self.smellLog[0][1] >= 2:
            pos, cnt = self.smellLog.popleft()
            if (pos, cnt+1) not in self.smellLog and (pos, cnt+2) not in self.smellLog:
                self.smell[pos[0]][pos[1]] = 0

MagicShark()

