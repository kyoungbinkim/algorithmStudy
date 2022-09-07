from sys import stdin

size=int(stdin.readline())
numlist = list(map(int, stdin.readline().split()))
numset= list(set(numlist))
numDict= {}
anslist = [0]*size
lenset = len(numset)

numset.sort()

for i in range(lenset):
    numDict.update({numset[i]:i})

# for i in range(lenset-1):
#     for j in range(i+1, lenset):
#         if numset[i] > numset[j]:
#             if numDict.get(numset[i]) == None:
#                 numDict.update({numset[i]:1})
#             else:
#                 numDict[numset[i]]+=1
#         else:
#             if numDict.get(numset[j]) == None:
#                 numDict.update({numset[j]:1})
#             else:
#                 numDict[numset[j]]+=1

for i in range(size-1):
    if numDict.get(numlist[i]) == None:
        print(0, end=" ")
    else:
        print(numDict[numlist[i]], end=" ")

if numDict.get(numlist[size-1]) == None:
    print(0)
else:
    print(numDict[numlist[size-1]])
    
