import os
from subprocess import check_output

with open('aaa','r') as f:
    line=f.read()
    print check_output(["cowsay",line])

    
