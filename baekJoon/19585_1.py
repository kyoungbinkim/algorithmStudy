from sys import stdin

class node:
    def __init__(self, key, flag=False):
        self.key = key
        self.child = {}
        self.flag = flag

class Trie:
    def __init__(self):
        self.rt = node(None)
    
    def update(self, s):
        current = self.rt

        for i in range(0, len(s), 2):
            key = s[i:i+2]
            if current.child.get(key) == None:
                current.child.update({key: node(key)})
            current = current.child[key]
        current.flag = True
    
    def search(self, s):
        current = self.rt

        for i in range(0, len(s), 2):
            key = s[i:i+2]
            child = current.child.get(key)
            if child == None:
                return False
            current = child
        return current.flag

        
c,n = map(int ,stdin.readline().split())
cset, nset = [], []
myTrie = Trie()

for _ in range(c):
    cset.append(stdin.readline().removesuffix('\n'))

for _ in range(n):
    nset.append(stdin.readline().removesuffix('\n'))

for color in cset:
    for name in nset:
        legend = color+name
        legend = legend if len(legend)%2==0 else legend + '0'
        myTrie.update(legend)

for _ in range(int(stdin.readline())):
    tmp = stdin.readline().removesuffix('\n')
    tmp = tmp if len(tmp)%2 == 0 else tmp+'0'
    if myTrie.search(tmp):
        print("Yes")
    else:
        print("No")
