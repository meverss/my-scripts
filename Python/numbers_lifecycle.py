from colored import fg, bg, attr
from random import randint as rnd
from os import popen
clear = popen('clear','r').read()
print(clear)

nlc,n1,left,l = [],[],[],''
red = fg('red')
normal = attr(0)

# Get screen size
size = popen('stty size', 'r').read().split()
for x in range(2):
  size[x] = int(size[x])

for a in range(1,10):
  a = str(a)
  n1.append(a)
  l  = ''.join(n1)
  l = int(l)
  left.append(l)

for x in range(9):
  formula = left[x]*8+(x+1)
  nlc.append(f"{left[x]} x {red}8{normal} + {x+1} = {formula}")

for line in nlc:
  print(line.center(size[1]+10))