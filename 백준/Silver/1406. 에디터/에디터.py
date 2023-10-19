from sys import stdin
from collections import deque

l, r = deque([c for c in stdin.readline().removesuffix('\n')]), deque()

for _ in range(int(stdin.readline())):
    cmd = list(stdin.readline().split())

    if cmd[0] == 'L' and len(l):
        r.appendleft(l.pop())
        
    elif cmd[0] == 'D' and len(r):
        l.append(r.popleft())
    elif cmd[0] == 'B' and len(l) :
        l.pop()
    elif cmd[0] == 'P':
        l.append(cmd[1])


ans = "".join(list(l))
ans = ans + "".join(list(r)) 

print(ans)