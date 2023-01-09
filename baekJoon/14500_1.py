from sys import stdin
import heapq

n,m = map(int, stdin.readline().split())
Board = []
for i in range(n):
    Board.append(list(map(int, stdin.readline().split())))



class technomino:
    
    def __init__(self, Board, n, m):
        self.dx = [-1,1,0,0]
        self.dy = [0,0, 1,-1]
        self.board = Board
        self.h = n
        self.w = m

    # [val, [x,y]]
    def BFS(self, x, y):
        visit = {}
        ans = 0
        heap = []
        heapq.heappush(heap,[-self.board[x][y],x,y])
        
        visit.update({str(x).zfill(3)+str(y).zfill(3) : True})

        for i in range(4):
            val, tmpx, tmpy = heapq.heappop(heap)
            ans += val
            visit.update({str(tmpx).zfill(3)+str(tmpy).zfill(3) : True})
            for j in range(4):
                if tmpx+self.dx[j] < 0 or tmpx+self.dx[j] >= self.h or tmpy+self.dy[j] < 0 or tmpy+self.dy[j] >= self.w:
                    continue
                if visit.get(str(tmpx+self.dx[j]).zfill(3)+str(tmpy+self.dy[j]).zfill(3)):
                    continue
                # print(i,j)
                heapq.heappush(heap, [
                    -self.board[tmpx+self.dx[j]][ tmpy+self.dy[j]],
                    tmpx+self.dx[j], tmpy+self.dy[j]
                ])

            # print(ans)a
        self.dx[0],self.dx[1] = self.dx[1],self.dx[0]
        self.dy[0],self.dy[1] = self.dy[1],self.dy[0]
        return ans

t = technomino(Board,n,m)
ans = 1

# print(t.BFS(2,3))

for i in range(n):
    for j in range(m):
        tmp = t.BFS(i,j)
        if tmp < ans:
            # print(i,j, tmp)
            ans = tmp
print(-ans)


