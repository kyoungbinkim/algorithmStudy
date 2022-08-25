from sys import stdin
import math

N = int(stdin.readline())
numDict = {}

for _ in range(N):
    ind1, ind2, a, b = map(int, stdin.readline().split())
    Gcd = math.gcd(a,b)
    a ,b = a//Gcd, b//Gcd

    dict1, dict2 = numDict.get(ind1), numDict.get(ind2)
    if dict1 == None and dict2 == None:
        numDict.update({ind1 : [[ind2, b]], ind2:[[ind1, a]]})
    elif dict1 == None or dict2 == None:

