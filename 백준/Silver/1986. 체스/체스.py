from sys import stdin


knightMove = [ (2,1), (2,-1), (-2,1), (-2,-1), (1,2), (-1,2), (1,-2), (-1,-2) ]
queenMove = [ (1,0), (0,1), (-1,0), (0, -1), (1,1), (-1,-1), (1,-1), (-1, 1) ]

n, m = map(int ,stdin.readline().split())
board = [[0 for _ in range(m)] for _ in range(n)]

queen = list(map(lambda x:int(x)-1, stdin.readline().split()))
knight  = list(map(lambda x:int(x)-1, stdin.readline().split()))
pawn   = list(map(lambda x:int(x)-1, stdin.readline().split()))

horses = set()

knight = [(knight[i], knight[i+1]) for i in range(1,len(knight), 2)]
queen = [(queen[i], queen[i+1]) for i in range(1,len(queen), 2)]
pawn = [(pawn[i], pawn[i+1]) for i in range(1,len(pawn), 2)]

horses = horses.union(set(knight))
horses = horses.union(set(queen))
horses = horses.union(set(pawn))

for pos in knight:
    for d in knightMove:
        dr, dc = pos[0] + d[0], pos[1] + d[1]

        if dr < 0 or dc < 0 or dr >=n or dc >= m:
            continue
        board[dr][dc] = 1

for pos in queen:
    for d in queenMove:
        dr, dc = pos[0] + d[0], pos[1] + d[1]
        while True:
            if dr < 0 or dc < 0 or dr >=n or dc >= m:
                break

            if (dr,dc) in horses:
                break

            board[dr][dc] = 1
            dr += d[0]
            dc += d[1]

for (r,c) in horses:
    board[r][c] = 1

# for b in board:
#     print(b)

print(n*m - sum([sum(x) for x in board]))