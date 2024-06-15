from sys import stdin
from heapq import heappush, heappop
from collections import deque

def solve():
    maxlen = 1
    maxcnt = 0
    n = int(stdin.readline())
    alpha = stdin.readline().strip()
    p = list(map(lambda x:int(x)-1, stdin.readline().split()))
    degs= [0 for _ in range(n)]
    ans = [[1,1, []] for _ in range(n)] # maxlen,  cnt, lens from childs
    
    for c in p:
        if c < 0:
            continue
        degs[c] += 1
    
    que = deque([])
    for i in range(n):
        if degs[i] == 0 and p[i] >= 0:
            que.append(i)
    # print("p : ", p)
    # print("degs : ", degs)
    
    vis = set()
    while len(que):
        i = que.popleft()
        # print(i)
        # print(ans, maxlen, maxcnt, vis)
        
            
        # print(i)
        vis.add(i)
        degs[p[i]] -= 1
        if degs[p[i]] == 0 and not p[i] in vis and p[p[i]] >= 0:
            que.append(p[i])

        if maxlen < ans[i][0]:
            maxlen = ans[i][0]
            maxcnt = ans[i][1]
        elif maxlen == ans[i][0]:
            maxcnt += ans[i][1]
                

                
        if len(ans[i][2]) > 1:
            tmp1 = heappop(ans[i][2])
            if tmp1[0] == ans[i][2][0][0]:
                if -2 * tmp1[0] +  1 >= maxlen:
                            maxcnt = maxcnt if maxlen == -2 * tmp1[0] +  1 else 0
                            maxlen = -2 * tmp1[0] +  1
                            tmp = [tmp1]

                            # print(ans[i][2], tmp1, tmp, "??")
                            while len(ans[i][2]) and tmp1[0] == ans[i][2][0][0]:
                                ttt = heappop(ans[i][2])
                                for can in tmp:
                                    maxcnt += can[1] * ttt[1]
                                tmp.append(ttt)
            else:
                        tmp = heappop(ans[i][2])

                        if -tmp[0]-tmp1[0] + 1 >= maxlen:
                            maxcnt = maxcnt+ tmp[1]*tmp1[1] if maxlen == -tmp[0]-tmp1[0] + 1 else tmp[1]*tmp1[1]
                            maxlen = -tmp[0]-tmp1[0] + 1
                            
                            while len(ans[i][2]) and tmp[0] == ans[i][2][0][0]:
                                ttt = heappop(ans[i][2])
                                maxcnt += tmp1[1] * ttt[1]
                    
                
        if alpha[i] == alpha[p[i]]:
            continue

                
        heappush(ans[p[i]][2], (-ans[i][0], ans[i][1]))

        if ans[p[i]][0] < ans[i][0]+1:
            ans[p[i]][0] = ans[i][0]+1
            ans[p[i]][1] = ans[i][1]
        elif ans[p[i]][0] == ans[i][0]+1:
            ans[p[i]][1] += ans[i][1]

    
    # print('~~', ans, maxlen, maxcnt, vis)

    for i in range(n):
        if p[i] < 0:
            if maxlen < ans[i][0]:
                maxlen = ans[i][0]
                maxcnt = ans[i][1]
            elif maxlen == ans[i][0]:
                maxcnt += ans[i][1]
                
            # print("!!", ans, maxlen, maxcnt, vis)
            if len(ans[i][2]) > 1:
                    tmp1 = heappop(ans[i][2])
                    # print(tmp1, ans[i][2])
                    if tmp1[0] == ans[i][2][0][0]:
                        if -2 * tmp1[0] +  1 >= maxlen:
                            maxcnt = maxcnt if maxlen == -2 * tmp1[0] +  1 else 0
                            maxlen = -2 * tmp1[0] +  1
                            tmp = [tmp1]

                            # print(ans[i][2], tmp1, tmp, "??")
                            while len(ans[i][2]) and tmp1[0] == ans[i][2][0][0]:
                                ttt = heappop(ans[i][2])
                                for can in tmp:
                                    maxcnt += can[1] * ttt[1]
                                tmp.append(ttt)
                    else:
                        tmp = heappop(ans[i][2])
                        if -tmp[0]-tmp1[0] + 1 >= maxlen:
                            maxcnt = maxcnt + tmp[1]*tmp1[1] if maxlen == -tmp[0]-tmp1[0] + 1 else tmp[1]*tmp1[1]
                            maxlen = -tmp[0]-tmp1[0] + 1
                            
                            while len(ans[i][2]) and tmp[0] == ans[i][2][0][0]:
                                ttt = heappop(ans[i][2])
                                maxcnt += tmp1[1] * ttt[1]
            break
    # print(ans, maxlen, maxcnt, vis)
    # print("!!!::", maxlen, maxcnt)
    print(maxlen, maxcnt)
          
for _ in range(int(stdin.readline())):
    solve()