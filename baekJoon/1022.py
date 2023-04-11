from sys import stdin

r1, c1, r2, c2  = map(int,stdin.readline().split())

def getPad(s, plen):
    return (plen - len(s)) * ' ' + s

def findVal(r,c):

    r_abs = abs(r)
    c_abs = abs(c)
    boxNum = max(r_abs, c_abs) # start 0

    if r_abs == c_abs:
        # r 이양수일 경우
        if r_abs == r:
            if c_abs == c:
                return (2*boxNum+1) ** 2
            else:
                return (2*boxNum - 1) ** 2 + 2*boxNum * 3
        
        # r이 음수일 경우
        else:
            if c_abs == c:
                return (2*boxNum - 1) ** 2 + 2*boxNum 
            else:
                return (2*boxNum - 1) ** 2 + 2*boxNum * 2
    
    # 오른쪽면 or 왼쪽면
    if c_abs == boxNum:

        # 오른쪽면
        if c_abs == c:
            return (2*boxNum - 1) ** 2 + (boxNum - r)
        #왼쪽면
        else:
            return (2*boxNum - 1) ** 2 +  (2*boxNum*2) +(boxNum + r)
    # 윗면 or 아래면
    else:
       if r_abs == r:
            return (2*boxNum - 1) ** 2 + (2*boxNum*3) + (boxNum + c)
       else:
            return (2*boxNum - 1) ** 2 + (2*boxNum) + (boxNum - c)


ansarr =[[]for _ in range(r2-r1+1)]
maxLen = 1
for i in range(r1, r2+1):
    for j in range(c1, c2+1):
        tmp = str(findVal(i,j))
        if len(tmp)> maxLen:
            maxLen = len(tmp)
        ansarr[i-r1].append(tmp)
# print(ansarr, maxLen)
for l in ansarr:
    for val in l:
        print(getPad(val, maxLen), end=' ')
    print()