"""
Title:    Christmast Tree
Author:   MeVeRsS
                                                           
Description:
This script shows a X-Mast Tree, with a random ornament
every time you run it.
"""

from colored import fg, bg, attr
from random import randint as rnd
from os import popen
clear = popen('clear','r').read()

# Get screen size
size = popen('stty size', 'r').read().split()
for x in range(len(size)):
  size[x] = int(size[x])

colors = ('white','green','red')
ornates = (f"{fg('red')}@{fg('green')}", f"{fg('white')}@{fg('green')}", f"{fg('blue')}@{fg('green')}")
leaves = f"{fg('green')}"
trunk = (f"{fg(130)}")
base = (f"{fg(240)}{attr(1)}")

text = list('MERRY CHRISTMAST!!')
for x in range(len(text)*2):
  if x%2 != 0 or x==0:
    text.insert(x,f"{fg(rnd(1,2))}")
text = ''.join(text)

print(clear)
print(f"{attr(1)}{(text).center(size[1])}")
print('')

print(('🌟').center(size[1]-5))
for i in range(2,20,2):
  oldct = f"{('*'*i)}"
  ct = list(oldct)
  ct[rnd(1,len(ct)-1)] = ornates[rnd(0,len(ornates)-1)]
  ct = ''.join(ct)
  ct = leaves + ct
  print((ct).center(82))

print(f"{trunk}{('[|]').center(size[1]-3)}")
print(base+('\_____/').center(size[1]-3))
print(size[1]*'-')
