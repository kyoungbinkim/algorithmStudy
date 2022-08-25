from sys import stdin

def run(q, ind):
    ans = 0
    while len(q) > 0:
        if q[0] == max(q):
            ans += 1
            if ind == 0:
                break
            del q[0]
        else:
            tmp = q[0]
            del q[0]
            q.append(tmp)
        
        ind -= 1
        if ind < 0:
            ind = len(q)-1

    print(ans)

for _ in range(int(stdin.readline())):
    queueLen, queueInd = map(int, stdin.readline().split())
    queue = list(map(int, stdin.readline().split()))

    run(queue, queueInd)
    
# 111 2 1 3 11 4
# 3 11 1112 
# 11 111 1


# 111 22 11 222 1 22 1
#     22 11 222 1 22 1 111
#           222 1 22 1 111 11
#               1 22 1 111 11
#                    1 111 11 1

# 111 23 11 222 1 22 1
#      3 11 222 1 22 1 111 2
#           222 1 22 1 111 2 11
#                 22 1 111 2 11 1
#                            11 1 1 111