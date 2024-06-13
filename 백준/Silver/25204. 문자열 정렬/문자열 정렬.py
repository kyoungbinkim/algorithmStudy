from sys import stdin

# print('A' < 'b')
# a>b 1  a==b 0 a<b -1
def compChar(a:str,b:str):
    if a == b:
        return 0
    if a == '-' and b =='-':
        return 0
    elif a == '-':
        return 1
    elif b == '-':
        return -1
    elif a.lower() > b.lower():
        return 1
    elif a.lower() == b.lower():
        return 1 if a > b else -1
    elif a.lower() < b.lower():
        return -1

def compStr(a:str,b:str):
    for i in range(min(len(a),len(b))):
        ret = compChar(a[i],b[i])
        if ret == 0:
            continue
        else:
            return ret
    return 1 if len(a) > len(b) else -1
    


def divideArr(arr):
    if len(arr) == 1:
        return arr
    mid = len(arr)//2
    return MergeArr(divideArr(arr[:mid]),divideArr(arr[mid:]))

def MergeArr(arr1,arr2):
    ans = []
    i = 0
    j = 0

    while i < len(arr1) and j < len(arr2):
        if compStr(arr1[i],arr2[j]) > 0:
            ans.append(arr2[j])
            j+=1
        else:
            ans.append(arr1[i])
            i+=1
    if i < len(arr1):
        ans += arr1[i:]
    elif j < len(arr2):
        ans += arr2[j:]
    return ans
    

for _ in range(int(stdin.readline())):
    srtarr = [stdin.readline().strip() for _ in range(int(stdin.readline()))]
    # print(srtarr)
    ret = divideArr(srtarr)
    # print(ret)
    print('\n'.join(ret))
    # print()