from sys import stdin
from copy import deepcopy

class ballExit:
    def __init__(self, b, row, col):
        self.row, self.col = row, col
        self.dir = {"up":[-1,0], "down":[1,0], "right":[0,1], "left":[0,-1], None:[0,0]}
        self.key = self.dir.keys()
        self.que = [[b,0,None]]
        self.board = None

    def check(self, board):
        for i in range(row):
            for j in range(col):
                if board[i][j] == 2:
                    return False
        return True

    def Go(self, direction):
        
        b = deepcopy(self.board)
        dy, dx= self.dir[direction]
        flag = False
        for r in range(0,row) if dx >= 0 else range(row-1, -1, -1):
            for c in range(0,col) if dy >= 0 else range(col-1, -1, -1):
                if 2<= b[r][c] <=3:
                    flag = True
                    tmp_r, tmp_c = r+dy,c+dx
                    while b[tmp_r][tmp_c] == 0:
                        if b[tmp_r][tmp_c] == 1:
                            break
                        tmp_r += dy
                        tmp_c += dx
                    
                    if b[tmp_r][tmp_c] == 1:
                        flag = False if b[r][c]==3 else flag
                        b[r][c] = 0
                    elif tmp_r-dy == r and tmp_c-dx == c:
                        continue
                    else:
                        b[tmp_r-dy][tmp_c-dx] = b[r][c]
                        b[r][c] = 0
        return flag, b
    
    def Run(self):
        
        while len(self.que)>0:
            b,cnt,before = self.que[0]
            self.que.pop(0)
            # print(cnt)
            if cnt >= 10:
                return -1

            self.board = b
            # self.printBoard(b)
            for k in self.key:
                if k==before or [self.dir[k][0] + self.dir[before][0], self.dir[k][1]+self.dir[before][1]] ==[0,0]:
                    continue
                f, hi= self.Go(k)
                if self.check(hi) and f:
                    return cnt+1
                if f:
                    self.que.append([hi, cnt+1,k])
                
        return -1        
        
    def printBoard(self,board):
        for b in board:
            print(b)
        print()


if __name__ == "__main__":
    c2i = {"#": -1, ".":0, "R":2, "B":3, "O":1}
    row,col = map(int, stdin.readline().split())
    Board = []
    for i in range(row):
        Board.append([c2i[x] for x in stdin.readline().removesuffix('\n')])
    # print(Board)

    bExit = ballExit(Board, row, col)
    print(bExit.Run())

