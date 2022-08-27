from sys import stdin

def calcPush(dest, n):
    if n == "100":
        return abs(int(dest) - int(n))
    return len(n) + abs(int(dest) - int(n))

def calcAns(l, dest):
    a = []
    for i in l:
        if type(i) == type(list([])):
            a.append(calcAns(i, dest))
        else:
            a.append(calcPush(dest, i))
    return min(a)

def getAns(dest:str, ans:str, s:set):
    
    if ans == '':
        a = []
        for k in s:
            a.append(getAns(dest, str(k), s))
        return a
    
    destLen = len(dest)
    ansLen = len(ans)
    if destLen == ansLen:
        return str(int(ans))
    if dest[ansLen-1] > ans[ansLen-1]:
        return str(int(ans + str(max(s))*(destLen-ansLen)))
    elif dest[ansLen-1] < ans[ansLen-1]:
        return str(int(ans + str(min(s))*(destLen-ansLen)))
    else:
        a = []
        for k in s:
            a.append(getAns(dest, ans+str(k), s))
        return a

    

target , delsize = stdin.readline().replace('\n', ''),int(stdin.readline())
S = set(range(10))
if delsize != 0:
    for tmp in stdin.readline().split():
        S.remove(int(tmp))
cand = getAns(target, '', S)
cand.append("100")
if len(S) != 0:
    if len(target) > 1:
        cand.append(str(int( str(max(S))*(len(target)-1) )))
    if 0 in S:
        t = S.copy()
        t.remove(0)
        if len(t) != 0:
            cand.append(str(int(str(min(t)) + str(min(S)) * len(target))))
    cand.append(str(int(str(min(S)) + str(min(S)) * len(target))))
print(calcAns(cand, target))