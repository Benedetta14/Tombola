import random

class TombolaGame:
    
    def __init__(self):
        self.tp = set()
        
    def add(self, p):
        if not isinstance(p, Player):
            raise TypeError('')
        self.tp.add(p)
        
    def extraction(self):
        numbers = [i for i in range(90)]
        nn = len(numbers)
        x = random.randint(0, nn-1)
        en = numbers[x]
        del numbers[x]
        return en
    
    def game(self):
        
        if len(self.tp) == 0:
            raise Exception('')
        
        glist = []
        for i in self.tp:
            for k in i.cartelle:
                 glist.append(k)
        gdict = {i.name:[0, 0, 0] for i in glist}
        winners = {'ambo':' ', 'terna':' ', 'quaterna':' ', 'cinquina':' '}
        a, t, q, c = 0, 0, 0, 0
        
        
        h = True
        while h == True:
            en = self.extraction()
            for cc in glist:
                for i in range(3):
                    gdict[cc.name][i] += cc.contain(en)[i]
                for k in gdict[cc.name]:
                    if a == 0:
                        if k == 2:
                            winners['ambo'] = cc.player.pname
                            #winners.append(cc.player.pname)
                            a += 1
                    if t == 0:
                        if k == 3:
                            winners['terna'] = cc.player.pname
                            t += 1
                    if q == 0:
                        if k == 4:
                            winners['quaterna'] = cc.player.pname
                            q += 1
                    if c == 0:
                        if k == 5:
                            winners['cinquina'] = cc.player.pname
                            c += 1
                if sum(gdict[cc.name]) == 15:
                    tombolawinner = {'The tombola winner is:':' '}
                    tombolawinner['The tombola winner is:'] = cc.player.pname
                    h = False
                    break
        
        return winners, tombolawinner
                
        
      
class Cartella:
    
    def __init__(self, player, name):
        if not isinstance(player, Player):
            raise TypeError('')
        self.player = player
        self.name = name
        self.r1 = [-1]*5
        self.r2 = [-1]*5
        self.r3 = [-1]*5
        self.l = [self.r1, self.r2, self.r3]
        player.add(self)
        
    def __setitem__(self, x, v):
        if not isinstance(x, int):
            raise TypeError('')
        if not isinstance(v, int):
            raise TypeError('')
        if not 0<=x<15:
            raise KeyError()
        if not 0<=v<90:
            raise ValueError('')
        if self.__contains__(v) == True:
            raise ValueError('')
        if x < 5:
            self.r1[x] = v
        elif 5 <= x < 10:
            x1 = x - 5
            self.r2[x1] = v
        else:
            x2 = x - 10
            self.r3[x2] = v
            
    def __repr__(self):
        s = str(self.name) + ':\n'
        for i in self.l:
            s += str(i) + '\n'
        return s
    
    def contain(self, x):
        if x in self.r1:
            return [1, 0, 0] 
        elif x in self.r2:
            return [0, 1, 0]
        elif x in self.r3:
            return [0, 0, 1]
        else:
            return [0, 0, 0]
        
    def __contains__(self, x):
        if x in self.r1:
            return True
        elif x in self.r2:
            return True
        elif x in self.r3:
            return True
        return False
        
        
class Player:
    
    def __init__(self, pname):
        if not isinstance(pname, str):
            raise TypeError('')
        self.pname = pname
        self.cartelle = []
        #self.m = len(self.cartelle)
    
    def add(self, v):
        if not isinstance(v, Cartella):
            raise TypeError('')
        self.cartelle.append(v)
        
    def __repr__(self):
        p = str(self.pname) + '[' + ', '.join(repr(i) for i in self.cartelle) + ']'
        return p
            
    
    
        
    