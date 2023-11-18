import math
from sys import stdin

def gcdExtended(a, b):
    if a == 0 :
        return b,0,1
             
    gcd,x1,y1 = gcdExtended(b%a, a)
     
    x = y1 - (b//a) * x1
    y = x1
     
    return gcd,x,y

def mergeCRT(a1, m1, a2, m2):
    l =math.lcm(m1,m2)
    g, p, q = gcdExtended(m1, m2)
    # print(a1, m1, a2, m2, g, p, q)
    if a1 % g != a2 % g:
        return -1, -1
    
    a = (a1 * m2 * q + a2 * m1 * p) // g
    return a%l, l
    

if __name__ == "__main__":
    n = int(stdin.readline())
    wordList = []
    lenList = []
    orderList = []
    for _ in range(n):
        tmp = stdin.readline().replace('\n', '')
        wordList.append(tmp)
        lenList.append(len(tmp))

    target = stdin.readline().replace('\n', '')
    for i in range(len(target)):
        
        for j in range(lenList[i]):
            if wordList[i][j] == target[i]:
                orderList.append(j)
                break
    
    if len(orderList) != len(wordList):
        print(-1)
    else:
        flag = True
        a, m = orderList[0], lenList[0]
        for i in range(1, n):
            a,m = mergeCRT(a,m, orderList[i], lenList[i])
            if a == -1:
                break
        print(a)
