def myDiff(A,B):
    ret = []
    for k in A.keys():
        if B.get(k) != None:
            ret.append(min([A[k], B[k]]))
    return sum(ret)

def myUnion(A,B):
    ret = {}
    
    for k in A.keys():
        if B.get(k) != None:
            ret.update({k: max([B[k], A[k]])})
        else:
            ret.update({k:A[k]})
            
    for k in B.keys():
        if A.get(k) != None:
            ret.update({k: max([B[k], A[k]])})
        else:
            ret.update({k:B[k]})
    ans = 0
    for k in ret.keys():
        ans += ret[k]
    # print(ret)
    return ans
    
def solution(str1, str2):
    
    A = {}
    B = {}
    
    for i in range(len(str1)-1):
        tmp = str1[i:i+2]
        if tmp.isalpha():
            if A.get(tmp.lower()) == None:
                A[tmp.lower()] = 0
            A[tmp.lower()] += 1
            
            
    for i in range(len(str2) -1):
        tmp = str2[i:i+2]
        if tmp.isalpha():
            if B.get(tmp.lower()) == None:
                B[tmp.lower()] = 0
            B[tmp.lower()] += 1
    print(A,B)
    d = myDiff(A,B)
    u = myUnion(A,B)
    
    if u == 0 :
        return 65536
    
    
    return int(d/ u * 65536) 