from colored import fg, bg, attr
from random import randint as rnd
from os import popen
clear = popen('clear','r').read()
print(clear)

red, normal = fg('red'), attr(0)

# Get screen size
size = list(int(x) for x in popen('stty size', 'r').read().split())

x = ''
for y in range(1,10):
  x += str(y)
  f = int(x)*8+y
  print((f"{x} x {red}8{normal} + {y} = {f}").center(size[1]+10))
