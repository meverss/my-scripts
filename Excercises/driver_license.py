from os import system
from colored import fg, bg, attr
import math
import getpass
from time_converter import convert
from PASSWORD import password
clear = system("clear")

## COLORS
title = (f"{fg('#cb4b16')}{attr(5)}")
quest = (f"{attr(0)}{fg(185) }")
normal = (f"{attr(0)}{fg('white')}")
error = (f"{attr(0)}{fg('red')}")

password()

print(f"{title}Driving License \nAuthor: MeVeRsS\n")
name = (input(f"{quest}¿Cuál es tu nombre? {normal}")).title()

try:
  agents = int(input(f"{quest}¿Cuántos agentes hay trabajando? {normal}"))
except ValueError:
  print(f"{error}Debe introducir un número entero{normal}")
others = input(f"{quest}¿Quien más está en la cola? {normal}")
cue = ((name + " " + others).title()).split(" ")
cue.sort()

my_turn = int((cue.index(name))+1)

if my_turn >= agents:
  rnd = math.ceil(my_turn / agents)
  license = rnd * 20
else:
  license = 20

print("\n"+name + ", tienes el " + str(cue.index(name) + 1) + " en la cola.")
print("Vas en la " + str(rnd) + " vuelta, así que tu licencia estará en " + str(convert(license)))