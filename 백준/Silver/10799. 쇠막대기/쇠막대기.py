from sys import stdin
from collections import deque

ans, tmp = 0, deque()

for c in stdin.readline().removesuffix('\n'):
    # print(tmp)
    if c == '(':
        tmp.append('(')
    
    if c == ')':
        if tmp[-1] == '(':
            tmp.pop()
            tmp.append(1)
        else:
            cnt = 0
            while tmp[-1] != '(':
                cnt += tmp.pop()
            tmp.pop()
            ans += (cnt + 1)
            tmp.append(cnt)
        
print(ans)