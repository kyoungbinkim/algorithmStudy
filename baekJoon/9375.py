from sys import stdin

for _ in range(int(stdin.readline())):
    fashion = {}
    size = int(stdin.readline())
    for _ in range(size):
        _, categ = stdin.readline().split()

        if fashion.get(categ) == None:
            fashion.update({categ:1})
        else:
            fashion[categ] +=1
    ans =1
    for k in fashion.keys():
        ans = ans*(fashion[k]+1)
    print(ans-1)