import random,sys,os;

class ruletka(object):
    def __init__(self):
        pass
    def play(self):
        return random.randint(0,36);
    
class player(object):
    allbets = {}
    
    def __init__(self,name):
        self.name=name
        
        
    bet = 0
    totalwins = 0
    
    def placebet(self,bet):
        
        self.bet = bet
        player.allbets[self] = bet
        
try:
    (numplayers,numgames) = sys.argv[1:3]
except ValueError:
    print "Not enough parameters"
    exit()

if not (numplayers.isdigit() or numgames.isdigit()):
    print "Invalid parameters"
    exit()

players=[]

for i in range(0,int(numplayers)):
    print i

    players.append(player(raw_input("Player %d name" % i)))

    print players[i].name

for i in range (0,int(numgames)):
    
    for p in players:
        
        pn=p.name
        print "game", i, "Player", p.name
        p.placebet(raw_input("Player %s place your bet" % pn))
        print "Player %s bet: " % pn, p.bet
        print "------------------"             

        #wynik=ruletka().play()       
        wynik="2"       

        print "ruletka: ", wynik
        for k,v in player.allbets.items():
            print k,v
            if v == wynik:
                k.totalwins +=1
                print "Player %s wins round %d" % (k.name, i) 
             
    for p in players:
        print "Player ", p.name, "won ", p.totalwins, "times" 

 