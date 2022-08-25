class Time:
    def __init__(self, t):
        self.h = int(t[:2])
        self.m = int(t[3:])
        # print(self.h, self.m)
    
    def Sum(self, time):
        self.m = self.m + time.m
        self.h = self.h + time.m
        if self.m >= 60:
            self.m -= 60
            self.h += 1
        return self.h*60 + self.m
    
    def Sub(self, time):
        self.h -= time.h
        if self.m < time.m:
            self.h -= 1
            self.m += 60
        self.m -= time.m
        return 60 * self.h + self.m

class Service:
    def __init__(self, fee):
        self.defaultTime = fee[0]
        self.defaultFee = fee[1]
        self.unitMin = fee[2]
        self.unitFee = fee[3]
        self.key = []
        self.record = {} # ID 2 [start, end]
    
    def upload(self, records):
        for rec in records:
            tmp = Parse(rec)
            if self.record.get(tmp[1]) == None:
                In = Time(tmp[0])
                self.record.update({tmp[1]: [In]})
                self.key.append(tmp[1])
            else:
                Out = Time(tmp[0])
                self.record[tmp[1]].append(Out)
        self.key.sort()
        return
        
    def calcFee(self):
        ret = []
        for key in self.key:
            ret.append(self.calcKey(key))
        return ret
    
    def calcKey(self, key):
        ret = 0
        totalMin = 0
        for t in range(0, len(self.record[key]), 2):
            if t == len(self.record[key]) -1 :
                totalMin += Time("23:59").Sub(self.record[key][t] )
            else:
                totalMin += self.record[key][t+1].Sub(self.record[key][t])
        
        if totalMin <= self.defaultTime:
            return self.defaultFee
                
        if (totalMin - self.defaultTime) % self.unitMin == 0:
            return self.defaultFee + ((totalMin - self.defaultTime) // self.unitMin) * self.unitFee
        else:
            return self.defaultFee + ((totalMin - self.defaultTime) // self.unitMin + 1) * self.unitFee
    
    
def Parse(rec):
    ret = []
    tmp =''
    for i in range(len(rec)):
        if rec[i] == ' ':
            ret.append(tmp)
            tmp = ''
        else:
            tmp += rec[i]
    ret.append(tmp)
    return ret

def solution(fees, records):
    S = Service(fees)
    S.upload(records)
    return S.calcFee()
    