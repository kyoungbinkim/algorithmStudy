from sys import stdin

for _ in range(int(stdin.readline())):
    numl = []
    for _ in range(int(stdin.readline())):
        numl.append(int(stdin.readline()))
    
    ans = 1
    while True:
        tmp = set()
        for n in numl:
            k = n%ans
            if n in tmp:
                break
            tmp.add(k)
        ans += 1
        if len(tmp) == len(numl):
            print(ans-1)
            break
        

