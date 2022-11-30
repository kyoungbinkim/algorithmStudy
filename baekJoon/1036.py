from sys import stdin

Dict = {}
numSize = int(stdin.readline())
numList = []
for _ in range(numSize):
    numList.append(stdin.readline().replace("\n", ""))
replaceSize = int(stdin.readline())

for n in numList:
    for s in n:
        Dict.update({s: True})
