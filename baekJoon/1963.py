import math
from sys import stdin

def isPrime(n):
    if n==2 or n==3:
        return True
    elif n==1 or n%2 ==0:
        return False

    for i in range(3, int(math.sqrt(n))+1, 2):
        if n%i ==0:
            return False
    return True

def comp(a,b):
    tmp = [1, 10, 100, 1000]
    cnt = 0

    for n in tmp:
        if a//n % 10 == b//n%10:
            cnt+=1
    if cnt == 3:
        return True
    return False

def getChild(a, plist, tmp):
    ans = set([])
    for p in plist:
        if comp(a,p) and p not in tmp:
            ans.add(p)
    # print(a, ans)
    return ans

def calc(a,b, plist):
    ans = set([a])
    
    cnt = 0
    while True:
        if b in ans:
            return cnt
        
        tmp = set()
        for i in ans:
            s = getChild(i, plist, ans)
            # print(s)
            tmp = tmp.union(s)
        # print("tmp ", tmp)
        if tmp == ans:
            return -1
        cnt += 1
        ans = tmp
    

primeList = []
for n in range(1000, 10000):
    if isPrime(n):
        primeList.append(n)

for _ in range(int(stdin.readline())):
    a,b = map(int, stdin.readline().split())
    ans = calc(a,b, primeList)
    if ans == -1:
        print("imposible")
    else:
        print(ans)


