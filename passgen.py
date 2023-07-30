import random
import string
from colorama import Fore

print(Fore.RED + r'''
___________________________________  
| _____ |   | ___ | ___ ___ | |   | |
| |   | |_| |__ | |_| __|____ | | | |
| | | |_________|__ |______ |___|_| |
| |_|   | _______ |______ |   | ____|
| ___ | |____ | |______ | |_| |____ |
|___|_|____ | |   ___ | |________ | |
| P A S S W O R D  G E N E R A T O R|
| | | ________| | __|____ | | | __| |
|_| |__ |   | __|__ | ____| | |_| __|
|   ____| | |____ | |__ |   |__ |__ |
| |_______|_______|___|___|___|_____|
--------------------------------------
        v1.0           author: dtlzz
--------------------------------------
''')
pas = ' '
pas1 = ' '
pas2 = ' '
vb = input("generate strong password. press c for custom press any key for default: ")
if vb == 'c':
    nu = int(input('how many numbers you want: '))
    char = int(input('how many character you want: '))
    letter = int(input('how many letter you want: '))
else:

    nu = random.randint(9, 19)
    char = random.randint(9, 19)
    letter = random.randint(9, 19)

for i in range(0, nu):
    gg = random.randint(0, 9)
    pas += str(gg)
for b in range(0, char):
    ff = random.choice(string.ascii_letters)
    pas1 += ff
for c in range(0, letter):
    dd = random.choice(string.punctuation)
    pas2 += dd
result = pas+pas2+pas1
lds = list(result)
random.shuffle(lds)
op = ' '
for iy in range(0, len(lds)):
    op = op + lds[iy]
print(Fore.GREEN+'\n your password is:\n' + op)
