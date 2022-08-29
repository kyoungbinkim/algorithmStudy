

d = {}
size = int(input())
for _ in range(size):
    s = input()
    if d.get(len(s)) == None:
        d.update({len(s): set([s])})
    else:
        d[len(s)].add(s)

keylist = list(d.keys())
keylist.sort()

for k in keylist:
    tmp = list(d[k])
    tmp.sort()
    for s in tmp:
        print(s)