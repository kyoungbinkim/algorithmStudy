from sys import stdin
from heapq import heappush, heappop

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
    # print("p : ", p)
    # print("degs : ", degs)
    
    vis = set()
    for _ in range(n):
        for i in range(n):
            if p[i] >= 0 and degs[i] == 0 and i not in vis:
                # print(i)
                vis.add(i)
                degs[p[i]] -= 1

                if maxlen < ans[i][0]:
                    maxlen = ans[i][0]
                    maxcnt = ans[i][1]
                elif maxlen == ans[i][0]:
                    maxcnt += ans[i][1]
                

                for tmp1 in range(len(ans[i][2])):
                    for tmp2 in range(tmp1+1, len(ans[i][2])):
                        idx1, idx2 = ans[i][2][tmp1], ans[i][2][tmp2]
                        if ans[idx1][0] + ans[idx2][0]+ 1> maxlen:
                            maxlen = ans[idx1][0] + ans[idx2][0]+ 1
                            maxcnt = ans[idx1][1] * ans[idx2][1]
                        elif ans[idx1][0] + ans[idx2][0]+ 1 == maxlen:
                            maxcnt += ans[idx1][1] * ans[idx2][1]
                
                if alpha[i] == alpha[p[i]]:
                    break

                
                ans[p[i]][2].append(i)

                if ans[p[i]][0] < ans[i][0]+1:
                    ans[p[i]][0] = ans[i][0]+1
                    ans[p[i]][1] = ans[i][1]
                elif ans[p[i]][0] == ans[i][0]+1:
                    ans[p[i]][1] += ans[i][1]
                break
    #     print(ans, maxlen, maxcnt, vis)
    # print(ans, maxlen, maxcnt, vis)

    for i in range(n):
        if p[i] < 0:
            if maxlen < ans[i][0]:
                maxlen = ans[i][0]
                maxcnt = ans[i][1]
            elif maxlen == ans[i][0]:
                maxcnt += ans[i][1]
                
            # print("!!", ans, maxlen, maxcnt, vis)
            for tmp1 in range(len(ans[i][2])-1):
                for tmp2 in range(tmp1+1, len(ans[i][2])):
                    idx1, idx2 = ans[i][2][tmp1], ans[i][2][tmp2]
                    if ans[idx1][0] + ans[idx2][0]+ 1> maxlen:
                        maxlen = ans[idx1][0] + ans[idx2][0]+ 1
                        maxcnt = ans[idx1][1] * ans[idx2][1]
                    elif ans[idx1][0] + ans[idx2][0]+ 1 == maxlen:
                        maxcnt += ans[idx1][1] * ans[idx2][1]
            break
    # print(ans, maxlen, maxcnt, vis)
    print(maxlen, maxcnt)
    


            
for _ in range(int(stdin.readline())):
    solve()