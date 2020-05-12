from colored import fg, bg, attr
import os, math
clear = os.system("clear")

from os import system
from colored import fg, bg, attr
clear = system("clear")

def convert(mins):
  if mins >= 60:
    formula = float(((mins//60)+((mins//60)*(mins-60*(mins//60)))/(mins//60*100)))
    formula = (f"{formula:.2f}")
    s_time = str(formula).split(".")
    time = (f"{s_time[0]}h:{s_time[1]}m")

    return time
  else:
    time = (f"{mins}m")
    return time

title = (f"{fg('#cb4b16')}{attr(5)}")
quest = (f"{attr(0)}{fg(69) }")
normal = (f"{attr(0)}{fg('white')}")
error = (f"{attr(0)}{fg('red')}")

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

import math

if my_turn >= agents:
  rnd = math.ceil(my_turn / agents)
  license = rnd * 20
else:
  license = 20

print("\n"+name + ", tienes el " + str(cue.index(name) + 1) + " en la cola.")
print("Vas en la " + str(rnd) + " vuelta, así que tu licencia estará en " + str(convert(license)))