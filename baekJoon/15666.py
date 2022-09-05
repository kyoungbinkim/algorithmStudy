from copy import deepcopy
from sys import stdin

def myPrint(arr):
    for i in range(len(arr)-1):
        print(arr[i], end=" ")
    print(arr[len(arr)-1])

def mySequence(arr, dep, ans, d):
    # print(arr, ans,d)
    if len(ans) == dep:
        if d.get(str(ans))==None:
            myPrint(ans)
            d.update({str(ans) : True})
        return

    for i in range(len(arr)):
        tmp = deepcopy(arr)
        tmp.remove(arr[i])
        mySequence(tmp, dep, ans+[arr[i]], d)

    

n,m = map(int, stdin.readline().split())
arr = list(map(int, stdin.readline().split()))
arr.sort()

mySequence(arr, m, [],{})