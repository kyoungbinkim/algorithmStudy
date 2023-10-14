from sys import stdin
from collections import deque

heaterDir = [(0,1), (0,- 1), (-1, 0), (1, 0)]
dir = heaterDir

class GoodByeHeater:
    def __init__(self):
        self.move = []
        self.makeMove()

        self.n, self.m, self.k = map(int ,stdin.readline().split())
        self.heaters = [[] for _ in range(4)]
        self.invest = set()

        self.board = [[0 for _ in range(self.m)] for _ in range(self.n)]

        for i in range(self.n):
            for (num, j) in zip(list(map(int, stdin.readline().split())), range(self.m)):
                if num:
                    if num == 5:
                        self.invest.add((i,j))
                    else:
                        self.heaters[num-1].append((i,j))

        self.wall = {}
        self.w = int(stdin.readline())

        for _ in range(self.w):
            r, c, s = map(int ,stdin.readline().split())
            r -= 1
            c -= 1
            dr,dc = (r-1, c) if s==0 else (r, c+1)
            if self.wall.get((r,c)) == None:
                self.wall[(r,c)] = set()
            if self.wall.get((dr,dc)) == None:
                self.wall[(dr,dc)] = set()

            self.wall[(r,c)].add((dr,dc))
            self.wall[(dr,dc)].add((r,c))


        for self.ans in range(1,101):
            for i in range(4):
                for (r,c) in self.heaters[i]:
                    dr,dc = r+dir[i][0], c+ dir[i][1]

                    if dr<0 or dc <0 or dr >=self.n or dc >= self.m:
                        continue

                    self.heat((dr,dc), i)

                    # for b in self.board:
                    #     print(b)
                    # print()
            self.updateBoard()
            # for b in self.board:
            #     print(b)
            # print()
            self.downBoarder()
            # for b in self.board:
            #     print(b)

            cnt = 0
            for (r,c) in self.invest:
                if self.board[r][c] >= self.k:
                    cnt += 1
            if cnt == len(self.invest):
                print(self.ans)
                return
        print(101)



    def makeMove(self):
        for i in range(4):
            moved = [heaterDir[i]]

            tmp = 1
            for _ in range(2):
                m = (0, tmp) if moved[0][0] != 0 else (tmp,0)
                moved.append(m)
                tmp *= -1
            self.move.append(moved)

    def heat(self, pos, select):
        visit = set([pos])
        que = deque([(pos, 5)])
        moved = self.move[select]

        while len(que):
            pos, power = que.popleft()
            self.board[pos[0]][pos[1]] += power

            if power == 1:
                continue

            r, c = pos
            dr, dc = pos[0] + moved[0][0], pos[1] + moved[0][1]
            # print("first Move : ", (r,c), (dr,dc), power)
            if dr < 0 or dc < 0 or dr >= self.n or dc >= self.m:
                continue

            if self.wall.get((r,c)) and (dr,dc) in self.wall[(r,c)]:
                pass
            else:
                if (dr,dc) not in visit:
                    que.append(((dr, dc), power-1))
                visit.add((dr,dc))


            for d in moved[1:]:
                r, c = pos
                dr = r + d[0]
                dc = c + d[1]
                if (dr,dc) in visit or dr < 0 or dc < 0 or dr >= self.n or dc >= self.m:
                    continue

                if self.wall.get((r,c)) and (dr, dc) in self.wall[(r,c)]:
                    continue

                r,c = dr,dc
                dr += moved[0][0]
                dc += moved[0][1]

                if (dr,dc) in visit or dr < 0 or dc < 0 or dr >= self.n or dc >= self.m:
                    continue

                if self.wall.get((r,c)) == None or (dr,dc) not in self.wall[(r,c)] and (dr,dc) not in visit:
                    que.append(((dr,dc), power-1))
                    visit.add((dr,dc))

    def updateBoard(self):
        newBoard = [[0 for _ in range(self.m)] for _ in range(self.n)]

        for i in range(self.n):
            for j in range(self.m):

                right = (i, j+1)
                down = (i+1, j)

                if right[1] < self.m and (self.wall.get((i,j)) == None or right not in self.wall[(i,j)] ):
                    diff = self.board[i][j] - self.board[right[0]][right[1]]


                    diff = (diff//4 + 1) if diff < 0 and diff % 4 else (diff // 4)

                    # print((i,j), right, diff)
                    newBoard[i][j] -= diff
                    newBoard[right[0]][right[1]] += diff

                if down[0] < self.n and (self.wall.get((i,j)) == None or down not in self.wall[(i,j)]):
                    diff = self.board[i][j] - self.board[down[0]][down[1]]

                    diff = (diff//4 + 1) if diff < 0 and diff % 4 else (diff // 4)
                    # print((i,j), down, diff)
                    newBoard[i][j] -= diff
                    newBoard[down[0]][down[1]] += diff

        for i in range(self.n):
            for j in range(self.m):
                self.board[i][j] += newBoard[i][j]

    def downBoarder(self):
        row = [0, self.n-1]
        col = [0, self.m-1]
        visit = set()
        for r in row:

            for j in range(col[0], col[1]+1):
                if self.board[r][j] and (r,j) not in visit:
                    visit.add((r,j))
                    self.board[r][j] -= 1

        for c in col:
            for i in range(row[0], row[1]+1):
                if self.board[i][c] and (i,j) not in visit:
                    visit.add((i,c))
                    self.board[i][c] -= 1

GoodByeHeater()