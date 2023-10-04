def solution(targets):

    targets.sort(key=lambda x : x[1])
    
    ans,end, idx = 0, 0, 0
    while True:
        end = targets[idx][1]
        ans += 1
        
        while targets[idx][0] < end:
            idx += 1
            if idx >= len(targets):
                break
        
        
        if idx >= len(targets):
            break
    return ans