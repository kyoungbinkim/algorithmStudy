from sys import stdin
from math import log, ceil

n= round(log(int(stdin.readline()), 3))

def expand(arr):
    wid = len(arr)
    ret = arr * 3

    for i in list(range(wid)) + list(range(wid*2 , wid*3)):
        ret[i] = ret[i]*3
    
    for i in range(wid*1, wid*2):
        ret[i] = ret[i] + ' '*wid + ret[i]
    return ret

base = ['*']
for i in range(n):
    base = expand(base)

for line in base:
    print(line)