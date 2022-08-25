def calc(s,n):
    ret = len(s)
    tmp = 0
    
    for i in range(n,len(s),n):
        if len(s[i:]) < n:
            break
        # print(s[i-n:i], s[i:i+n],i)
        if tmp == 0 and s[i-n:i] == s[i:i+n]:
            tmp += 1
            ret -= (n-1)
        elif tmp > 0 and s[i-n:i] == s[i:i+n]:
            ret -= n
            tmp += 1
            if tmp ==9:
                ret += 1
            elif tmp == 99:
                ret += 1
            elif tmp == 999:
                ret +=1
        else:
            tmp = 0
    # print(ret)
    return ret

def solution(s):
    answer = len(s)
    for i in range(1, len(s)//2+2):
        tmp = calc(s,i)
        if tmp < answer:
            answer = tmp
    return answer