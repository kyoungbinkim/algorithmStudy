from sys import stdin
import math

def getDivisor(n):
    ret = set([])
    for i in range(1, int(math.sqrt(n))+1):
        if n%i == 0:
            ret.add(i)
            ret.add(n//i)
    return ret


Map = {}
numList = []
for _ in range(int(stdin.readline())):
    num = int(stdin.readline())
    numList.append(num)
    if Map.get(num) == None:
        Map.update({num: 1})
    else:
        Map[num] += 1
for num in numList:
    ret= -1
    for tmp in getDivisor(num):
        if Map.get(tmp) != None:
            ret += Map[tmp]
    print(ret)
