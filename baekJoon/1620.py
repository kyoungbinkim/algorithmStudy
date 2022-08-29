from sys import stdin

n,m = map(int, stdin.readline().split())
id2ind, ind2id = {},{}

for i in range(n):
    s = stdin.readline().replace('\n','')
    id2ind.update({s : i+1})
    ind2id.update({i+1 : s})

for i in range(m):
    s = stdin.readline().replace('\n','')

    if s.isnumeric():
        print(ind2id[int(s)])
    else:
        print(id2ind[s])