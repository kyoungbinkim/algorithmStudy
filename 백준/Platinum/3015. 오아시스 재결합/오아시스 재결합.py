from sys import stdin
from collections import deque

n = int(stdin.readline())
stk, ans = deque([(int(stdin.readline()), 1, 1)]), 0

for idx in range(2, n+1):
    l = int(stdin.readline())
    isPop = False
    near = False

    while len(stk) and stk[-1][0] < l:
        tmp = stk.pop()
        ans += tmp[2]
        if tmp[1] == idx-1:
            near = True
        isPop = True
    
    # print()
    # print(near, isPop)
        
    if len(stk) and stk[-1][0] == l:
        tmp = stk.pop()
        new = (l, idx, tmp[2] + 1)
        if len(stk):
            ans += 1
        stk.append(new)
        ans += new[2]-1

        if new[1] == idx-1:
            near = True
    else:
        if not near or not isPop:
            ans += 1
        
        if len(stk) and isPop and stk[-1][0] > l:
            ans += 1

        stk.append((l, idx, 1))

    # if not isPop:
    #     ans += 1     
    # print(stk, ans)
print(ans)