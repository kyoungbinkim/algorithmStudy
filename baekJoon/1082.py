from sys import stdin

num2val = {}
val2num = {}
N = int(stdin.readline())
priceList = list(map(int ,stdin.readline().split()))
M = int(stdin.readline())

minPrice = min(priceList)

for i in range(len(priceList)):
    num2val.update({i:priceList[i]})
    val2num.update({priceList[i]:i})

ansList = []
for i in range(N):
    tmp = [i]
    tar = M - num2val[i]
    if tar < 0:
        continue
    

