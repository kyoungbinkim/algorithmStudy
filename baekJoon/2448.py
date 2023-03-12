from math import log2, ceil

hi  = 3
wid = 5
size = int(input())

arr = [
    '  *  ',
    ' * * ',
    '*****'
]

n = round(log2(size / 3))


for _ in range(n):
    padSize = ceil(wid/2)
    for i in range(hi):
        arr.append(arr[i]+' ' +arr[i])
    for i in range(hi):
        arr[i] = ' '*padSize + arr[i] + ' ' * padSize
    
    wid = wid *2+1
    hi = hi*2


for l in arr:
    print(l)

    

    

