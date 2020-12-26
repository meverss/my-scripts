from colored import fg, bg, attr
from random import randint
from os import system, popen
clear = system("clear")

# Get screen size
size = popen('stty size', 'r').read().split()
for x in range(len(size)):
  size[x] = int(size[x])

colors = ('white','green','red')
trunk = (f"{fg(130)}")
base = (f"{fg(240)}{attr(1)}")
tree = ''

print(('MERRY CHRISTMAST!!').center(size[1]))
print('')

print(('🌟').center(size[1]-1))
for i in range(2,20,2):
  if i%4 == 0:
    tree = f"{tree}{fg(colors[randint(0,2)])}"
  else:
    tree = f"{fg('green')}"
  print(f"{tree}{('*'*i).center(size[1]-1)}")
    

print(f"{trunk}{('|||').center(size[1]-1)}")
print(base+('\_____/').center(size[1]-1))
print(size[1]*'-')
