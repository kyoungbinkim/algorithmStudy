from sys import stdin
from collections import deque

sharkDir = [(0, -1), (1,0), (0,1), (-1,0)]
magicDir = [(-1,0), (1,0), (0,-1), (0, 1)]

class MagicShark:
    def __init__(self):
        self.ans = 0

        self.n, self.m = map(int, stdin.readline().split())
        self.shark = (self.n//2, self.n//2)

        self.makeSequence()

        self.board = [list(map(int, stdin.readline().split())) for _ in range(self.n)]

        self.magic = []

        for _ in range(self.m):
            d, s = map(int, stdin.readline().split())
            self.magic.append((d-1, s))

        for i in range(self.m):
            self.blizzard(i)
            self.moveShark()

            while self.destoryShark():
                self.moveShark()

            self.updateShark()
        print(self.ans)

    def blizzard(self, idx):
        d, s = self.magic[idx]

        for i in range(1, s+1):
            dr, dc = self.shark[0] + magicDir[d][0] * i, self.shark[1] + magicDir[d][1] * i

            if dr < 0 or dc <0 or dr >=self.n or dc>= self.n:
                break

            # self.ans += self.board[dr][dc]
            self.board[dr][dc] = 0

    def makeSequence(self):
        self.seq = [self.shark]

        num = 1
        cnt = 0
        d = 0
        while self.seq[-1] != (0,0):

            if cnt == 2:
                cnt = 0
                num += 1

            for _ in range(num):
                dr,dc = self.seq[-1][0] + sharkDir[d][0], self.seq[-1][1] + sharkDir[d][1]
                if dr < 0 or dc < 0:
                    break
                self.seq.append((dr,dc))
            cnt += 1
            d = (d + 1) % 4

    def moveShark(self):

        empty = deque()

        for pos in self.seq[1:]:

            if self.board[pos[0]][pos[1]] == 0:
                empty.append(pos)
            elif len(empty):
                newPos = empty.popleft()

                self.board[newPos[0]][newPos[1]] = self.board[pos[0]][pos[1]]
                self.board[pos[0]][pos[1]] = 0

                empty.append(pos)

    def destoryShark(self):
        FLAG = False
        visit, num = set([self.seq[1]]), self.board[self.seq[1][0]][self.seq[1][1]]

        for pos in self.seq[2:]:

            if self.board[pos[0]][pos[1]] == num:
                visit.add(pos)
            else:
                if len(visit) >= 4:
                    FLAG = True
                    self.ans += num * len(visit)
                    for (r,c) in visit:
                        self.board[r][c] = 0
                visit = set([pos])
                num = self.board[pos[0]][pos[1]]
        return FLAG

    def updateShark(self):
        update = []
        visit, num = set([self.seq[1]]), self.board[self.seq[1][0]][self.seq[1][1]]

        for pos in self.seq[2:]:
            if self.board[pos[0]][pos[1]] == num:
                visit.add(pos)
            else:
                update += [len(visit), num]

                visit = set([pos])
                num = self.board[pos[0]][pos[1]]

        newBoard = [[0 for _ in range(self.n)] for _ in range(self.n)]

        for i in range(min(self.n * self.n -1, len(update) )):
            newBoard[self.seq[i+1][0]][self.seq[i+1][1]] = update[i]
        self.board = newBoard

MagicShark()