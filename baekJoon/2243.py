from sys import stdin

global keys
keys = []
def insert(c, val, num):
    global keys
    if c.get(val) == None:
        c.update({val : num})
        updateKey(keys, val)
    else:
        c[val] += num
        c[val] = 0 if c[val] < 0 else c[val]

def remove(c,ind):
    cnt = 0
    for k in keys:
        cnt += c[k]
        if cnt >= ind:
            c[k] -= 1
            return k

def updateKey(keys, val):
    if len(keys) < 2:
        keys.append(val)
        keys.sort(reverse=False)
        # print(keys)
        return
    start,end = 0, len(keys)-1
    mid = (start+end) // 2
    # print(start,end, mid)
    while start < end:
        if keys[mid] < val:
            start = mid + 1
        else:
            end = mid - 1
        
        if keys[mid] < val <keys[mid+1]:
            break
        mid = (start+end) // 2 
    if(mid == 0):
        
        keys.insert(mid, val)
        # print(keys)
        return
    keys.insert(mid+1, val)
    # print(keys)

# updateKey([1,2,3,4,5,8,11,15,200,400], 201)
# updateKey([1,2,3,4,5,8,11,15,200,400], 401)
# updateKey([1,2,3,4,5,8,11,15,200,400], 7)
# updateKey([1,2,3,4,5,8,11,15,200,400], 0)
# updateKey([1,2], 0)
# updateKey([1,2], 3)

# updateKey([1], 2)

candy = {}
n = int(stdin.readline())

for _ in range(n):
    cmd = list(map(int, stdin.readline().split()))
    # print(cmd)
    if len(cmd) == 2:
        # print('ans' ,remove(candy, cmd[1]), candy, keys)
        print( remove(candy, cmd[1]))
    else:
        insert(candy, cmd[1], cmd[2])
    print(candy, keys)


# 10
# 2 2 2
# 1 2
# 2 1 3
# 2 3 3
# 1 2
# 1 2
# 2 1 1
# 1 2
# 1 1
# 1 1