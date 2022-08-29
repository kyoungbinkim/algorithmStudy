from sys import stdin

def strSum(string):
    ret = 0
    for s in string:
        if s.isnumeric():
            ret += int(s)
    return ret

def isSmall(s1 ,s2): # if s1 < s2 : true
    if len(s1) < len(s2) :
        return True
    elif len(s1) > len(s2) :
        return False
    elif strSum(s1) < strSum(s2):
        return True
    elif strSum(s1) > strSum(s2):
        return False
    elif s1 < s2:
        return True
    return False


readLine = stdin.readline
arr= []
for _ in range(int(readLine())):
    arr.append(input())

for i in range(len(arr)-1):
    MinInd = i
    for j in range(i+1, len(arr)):
        if isSmall(arr[j], arr[MinInd]):
            MinInd = j
    
    tmp = arr[MinInd]
    arr[MinInd] = arr[i]
    arr[i] = tmp

for s in arr:
    print(s)

