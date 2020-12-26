from colored import fg, bg, attr
from random import randint as rnd
from os import system, popen
clear = system("clear")

# Get screen size
size = popen('stty size', 'r').read().split()
for x in range(len(size)):
  size[x] = int(size[x])

colors = ('white','green','red')
ornates = ('🔵','🔴','⚪')
trunk = (f"{fg(130)}")
base = (f"{fg(240)}{attr(1)}")
tree = ''

print(('MERRY CHRISTMAST!!').center(size[1]))
print('')

print(('🌟').center(size[1]-5))
for i in range(2,20,2):
  if i%4 == 0:
    tree = f"{fg(colors[rnd(0,2)])}"
  else:
    tree = f"{fg('green')}"
  oldct = '@'*i
  ct = list(oldct)
  if len(ct) >= 4:
    ct[rnd(1,len(ct)-2)] = ornates[rnd(0,len(ornates)-1)]

  ct = ''.join(ct)
  print(f"{tree}{(ct).center(size[1]-5)}")

print(f"{trunk}{('|||').center(size[1]-3)}")
print(base+('\_____/').center(size[1]-3))
print(size[1]*'-')
