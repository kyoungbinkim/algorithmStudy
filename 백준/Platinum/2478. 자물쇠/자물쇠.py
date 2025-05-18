from copy import deepcopy
from sys import stdin
from collections import deque

import random

def chunck_list(l):
    ret = [[l[0], l[0]]]
    
    for e in l[1:]:
        if abs(ret[-1][1]- e) == 1:
            ret[-1][1] = e
        else:
            ret.append([e,e])
    return ret

def updateList(ans):
    ret = [ans[0]]
    for a in ans[1:]:
        if a[0] - ret[-1][1] == 1:
            ret[-1][1] = a[1]
        else:
            ret.append(a)
    return ret

def flip(seq):
    
    l = chunck_list(seq)
    if len(l) == 1 or len(l) > 4:
        return (None, None, None)
    p,q = float('inf'), -float('inf')
    
    for i in range(len(l)):
        ans = deepcopy(l)
        if ans[i][0] > ans[i][1]:
            ans[i][0],ans[i][1] = ans[i][1], ans[i][0]

            ans = updateList(ans)
            # print(ans)
            
            if any([a>b for a,b in ans]):
                continue
            
            if len(ans) == 2:
                p,q = seq.index(l[i][0]), seq.index(l[i][1])
                return p,q, ans
    
    for i in range(len(l) - 1):
        ans = deepcopy(l)
        ans[i][0],ans[i][1] = ans[i][1], ans[i][0]
        ans[i+1][0],ans[i+1][1] = ans[i+1][1], ans[i+1][0]
        ans[i],ans[i+1] = ans[i+1], ans[i]
        ans = updateList(ans)
        
        if any([a>b for a,b in ans]):
                continue
        
        if len(ans) == 2:
            p = seq.index(l[i][0])
            q = seq.index(l[i+1][1])
            return p,q, ans

    return (None, None, None)
    
def k_push(seq, k):
    return seq[k:] + seq[:k]

def pq_flip(seq, p, q):
    seq[p:q+1] = seq[p:q+1][::-1]
    return seq

def sol(n, l):
    
    for k2 in range(1, n):
        seq = l[-k2:] + l[:-k2]
        
        p,q,ans = flip(seq)
        
        if p == None or q==None:
            continue
        seq = pq_flip(seq,p, q)
        print(ans[-1][-1])
        print(f"{p+1} {q+1}")
        print(f"{k2}")
        
        return ans[-1][-1], p+1, q+1, k2

n = int(stdin.readline())
l = list(map(int, stdin.readline().split()))
sol(n, l)

