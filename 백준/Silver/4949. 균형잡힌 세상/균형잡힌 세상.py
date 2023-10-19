from sys import stdin
from collections import deque

chars = ['(', '[', '{']

charsMap = {
    ')' : chars[0],
    ']' : chars[1],
    '}' : chars[2]
}

while 1:
    s = stdin.readline().removesuffix('\n')
    if s =='.':
        break

    BREAK = False
    que = deque()

    for (i, c) in enumerate(s):

        if c in chars:
            que.append(c)
        elif c in charsMap.keys():

            if len(que) == 0 or que.pop() != charsMap[c]:
                BREAK = True
                break
        if BREAK:
            break
    
    if BREAK or len(que):
        print('no')
    else:
        print('yes')

