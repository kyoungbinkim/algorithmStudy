from sys import stdin

s = set()
for _ in range(int(stdin.readline())):
    tmp = stdin.readline().split()

    if tmp[0] == "add":
        s.add(int(tmp[1]))
    elif tmp[0] == "remove":
        if int(tmp[1]) in s:
            s.remove(int(tmp[1]))
    elif tmp[0] == "check":
        print(int(int(tmp[1]) in s))
    elif tmp[0] == "toggle":
        if int(tmp[1]) in s:
            s.remove(int(tmp[1]))
        else:
            s.add(int(tmp[1]))
    elif tmp[0] == "all":
        s = set(list(range(1,21)))
    elif tmp[0] == "empty":
        s= set()