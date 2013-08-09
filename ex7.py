# ex 7

import sys,cardreader,re

reload(cardreader)
#inputfile=sys.argv[1]
inputfile="card"
with open(inputfile,'r') as f:
    card=(f.read()).splitlines()


if (cardreader.validate(card)):
    cardreader.calculate(card)

