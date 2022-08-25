from sys import stdin
# text = list(map(int, stdin.read().replace('\n',' ').split()))
# print(text)
for n in stdin:
    n = int(n)
    i = 1
    while True:
        if i % n == 0:
            print(len(str(i)))
            break
        i = i*10 + 1