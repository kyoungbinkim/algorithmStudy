import numpy as np

def mySort(tmp):
    
    for i in range(len(tmp)):
        for j in range(i, len(tmp)):
            if tmp[i][0] < tmp[j][0] or \
            (tmp[i][0] == tmp[j][0] and tmp[i][1] > tmp[j][1]):    
                t= tmp[i]
                tmp[i] = tmp [j]
                tmp[j] = t
            

def solution(N, stages):
    tmp = []
    ans = []
    npStages = np.array(stages)    
    
    for i in range(1, N+1):
        fault = np.sum(npStages == i) / np.sum(npStages >= i)
        tmp.append([fault, i])
    
    mySort(tmp)
    
    for t in tmp:
        ans.append(t[1])
    print(ans)
    
    return ans