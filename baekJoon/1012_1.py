from sys import stdin
import sys

def getArr(mapArr,p, n):
    go = [(-1,0), (0,1), (0,-1), (1,0)]
    for x,y in go:
        x1 = x+p[0]
        y2 = y+p[1]
        if x1<0 or x1>=len(mapArr) or y2<0 or y2>=len(mapArr[0]):
            continue
        if mapArr[x1][y2] == n:
            mapArr[x1][y2] = n
            return True
    return False

if __name__ == "__main__":

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
        
        flag = True
        cnt = 1
        while flag:
            flag= False
            k = False
            for i in range(len(mapArr)):
                for j in range(len(mapArr[0])):
                    if mapArr[i][j] == 1 and not k:
                        flag = True
                        k = True
                        cnt += 1
                        mapArr[i][j] = cnt
                    getArr(mapArr,[i,j], cnt)
        for k in mapArr:
            print(k)                    