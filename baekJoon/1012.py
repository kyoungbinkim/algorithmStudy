from sys import stdin
import sys
def calc(mapArr, p): # x 세로 y가로
    go = [(-1,0), (0,1), (0,-1), (1,0)]
    mapArr[p[0]][p[1]] = 2
    for x,y in go:
        x1 = x+p[0]
        y2 = y+p[1]
        if x1<0 or x1>=len(mapArr) or y2<0 or y2>=len(mapArr[0]):
            continue
        if mapArr[x1][y2] == 1:
            calc(mapArr, [x1,y2])

if __name__ == "__main__":
    sys.setrecursionlimit(10**7)
    for _ in range(int(stdin.readline())):
        w, h, pSize = map(int, stdin.readline().split())
        mapArr = []
        tmp = []
        for _ in range(w):
            tmp.append(0)
        for _ in range(h):
            mapArr.append(tmp.copy())

        for _ in range(pSize):
            x,y = map(int, stdin.readline().split())
            mapArr[y][x] = 1
        
        ans = 0
        for i in range(len(mapArr)):
            for j in range(len(mapArr[0])):
                if mapArr[i][j] == 1:
                    calc(mapArr, [i,j])
                    ans +=1
        print(ans)
    

# def calc2(mapArr, p):
#     mapArr[p[0]][p[1]] = 2
#     if p[0]+1 < len(mapArr):
#         if mapArr[p[0]+1][p[1]] == 1:
#             calc2(mapArr, [p[0]+1, p[1]])
            
#     if p[1]+1 < len(mapArr[0]):
#         if mapArr[p[0]][p[1]+1] == 1:
#             calc2(mapArr, [p[0], p[1]+1])
            
#     if p[1] - 1 >= 0:
#         if mapArr[p[0]][p[1]-1] == 1:
#             calc2(mapArr, [p[0], p[1]-1])
            
#     if p[0] -1 >= 0:
#         if mapArr[p[0]-1][p[1]] == 1:
#             calc2(mapArr, [p[0]-1, p[1]])
        
#     return