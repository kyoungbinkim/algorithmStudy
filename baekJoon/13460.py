from sys import stdin

class ballExit:
    def __init__(self, b, row, col):
        self.dir = {"up":[-1,0], "down":[1,0], "right":[0,1], "left":[0,-1]}
        self.board = b
        self.red, self.blue = [],[]
        self.que = []
        for r in range(row):
            for c in range(col):
                if self.board[r][c] == 2:
                    self.red.append([r,c])
                    self.board[r][c] = 0
                elif self.board[r][c] == 3:
                    self.blue.append([r,c])
                    self.board[r][c] = 0
    
    def Go(self, direction):
        ans_r, ans_b = [],[]
        dy, dx = self.dir[direction]
        if dy!= 0:
            self.red.sort(key=lambda x : x[0]*dy)
            self.blue.sort(key=lambda x : x[0]*dy)
        else:
            self.red.sort(key=lambda x : x[1]*dx)
            self.blue.sort(key=lambda x : x[1]*dx)

        for r in self.red:
            y,x = r
            while self.board[y+dy][x+dx] == 0 and not [y+dy,x+dx] in ans_r:
                y += dy
                x += dx
            if self.board[y+dy][x+dx] == 1:
                continue
            ans_r.append([y,x])
        
        for b in self.blue:
            y,x = b
            while self.board[y+dy][x+dx] == 0 and not [y+dy,x+dx] in ans_r:
                y += dy
                x += dx
            if self.board[y+dy][x+dx] == 1:
                return False, None, None
            ans_b.append([y,x])
        
        return True, ans_r, ans_b
    
    def run(self):
        ans = 0
        key = self.dir.keys()
        self.que.append([self.red, self.blue, 0])

        while len(self.que) > 0:
            self.red, self.blue, cnt = self.que[0]
            self.que.pop(0)

            if cnt == 10:
                return -1
            
            for k in key:
                flag, r, b =self.Go(k)
                if flag:
                    if len(r) == 0:
                        return cnt+1
                    self.que.append([r,b,cnt+1])





if __name__ == "__main__":
    c2i = {"#": -1, ".":0, "R":2, "B":3, "O":1}
    row,col = map(int, stdin.readline().split())
    Board = []
    for i in range(row):
        Board.append([c2i[x] for x in stdin.readline().removesuffix('\n')])
    print(Board)

    bExit = ballExit(Board, row, col)
    print(bExit.run())

