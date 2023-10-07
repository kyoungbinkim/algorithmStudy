from sys import stdin

# 0 -> main, 1,2,3
line2 = [10, 13, 16, 19, 25]
line3 = [20, 22, 24, 25]
line4 = [30, 28, 27, 26, 25]
lines = [[], line2, line3, line4]

class Play:
    def __init__(self):
        self.horse = [0 for _ in range(4)]
        self.line = [0 for _ in range(4)]

        self.dices = list(map(int, stdin.readline().split()))
        
        tmp = self.moveDice(0, self.dices[0], self.line[0])
        self.horse[0] = tmp[0]
        self.line[0] = tmp[1]
        # print(self.horse, self.line)
        print(self.run(self.horse, self.line, tmp[0], 1))
        

    def run(self, h, l, score, idx):
        if idx >= 10:
            return score
        
        ans = 0 
        for i in range(4):
            if h[i] < 0:
                continue

            tmp = self.moveDice(h[i], self.dices[idx], l[i])
            # print(idx, tmp, h, l)
            if tmp[0] > 0 and tmp[0] in h and l[h.index(tmp[0])] == tmp[1]:
                # print(h[i], self.dices[idx], l[i])
                # print(tmp, h, l, l[h.index(tmp[0])] == tmp[1])
                # print()
                continue

            newh, newl = h.copy(), l.copy()
            newh[i] = tmp[0]
            newl[i] = tmp[1]

            newAns = self.run(newh,newl, score+tmp[0] if tmp[0] > 0 else score, idx+1)
            ans= max(ans, newAns)
        return ans
    
    def moveDice(self, idx, num, selector):

        if idx >= 40:
            return (-1, -1)
        if selector == 0:
            new = idx + num * 2
            if new > 40:
                return (-1, -1)
            elif new == 40:
                return (40, 4)
            return (new, new//10 if new < 40 and new%10 == 0 else 0 ) 
        elif 1 <= selector <= 3 :
            for (tmp, i) in zip(lines[selector], range(len(lines[selector]))):
                if tmp == idx:
                    lineIdx = i
                    break
            
            movedIdx = lineIdx + num

            if movedIdx >= len(lines[selector]) - 1:
                new = (25 + 5 * (movedIdx - len(lines[selector]) + 1), 4)
                return new if new[0] <= 40 else (-1, -1)

            return (lines[selector][movedIdx], selector)
        elif selector == 4:
            new = (idx + num * 5, 4)
            return new if new[0] <= 40 else (-1, -1)
        
Play()