import random,sys,os;

class ruletka(object):
    def __init__(self):
        pass
    def play(self):
        return random.randint(0,36);
    
class player(object):
    allbets = {}
    stats = {}
    players = []
    
    def __init__(self,name):
        self.name=name
        
        
    bet = 0
    totalwins = 0
    
    def placebet(self,bet):
        if ((0 <= bet) and (bet <= 36)):
            self.bet = bet
            player.allbets[self] = bet
        else:
            print "Bet out of range: ", bet

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

    player.players.append(player(raw_input("Player %d name: " % i)))

    print player.players[i].name

for i in range (0,int(numgames)):
    
    for p in player.players:
        
        pn=p.name
        print "Game: ", i, "Player: ", pn
        p.placebet(int(raw_input("Player %s place your bet: " % pn)))
        print "Player %s bets: " % pn, p.bet

    wynik=ruletka().play()       
    #wynik=2       

    print "Ruletka: ", wynik
    roundresult=[]
    for k,v in player.allbets.items():
        if v == wynik:
            k.totalwins +=1
            roundresult.append(k.name)
            print "Player %s won round %d " % (k.name, i) 
        else:
            print "Player %s lost round %d " % (k.name, i)
            roundresult.append('')
    
    player.stats[i]=(wynik,roundresult)

print "\n"         
for p in player.players:
    print "Player ", p.name, "won ", p.totalwins, "times" 

print "Summary\nRound  Result    Winners\n"

for k,v in ((player.stats).items()):
    round = str(k)
    wynik = str(v[0])
    winners = " ".join(v[1]).lstrip()
    print "%3s %7s       %-20s" % (round,wynik,winners)
    