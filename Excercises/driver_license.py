from colored import fg, bg, attr
import os, math
clear = os.system("clear")

from os import system
from colored import fg, bg, attr
import PASSWORD
clear = system("clear")

from os import system
from colored import fg, bg, attr

cls = system("clear")

## COLORS
title = (f"{fg('#cb4b16')}{attr(5)}")
quest = (f"{attr(0)}{fg(185) }")
normal = (f"{attr(0)}{fg('white')}")
error = (f"{attr(0)}{fg('red')}")

def convert(mins):

  def Time():
    formula = float((mins//60)+((mins//60)*(mins-60*(mins//60)))/(mins//60*100))
    formula = (f"{formula:.2f}") ## Here '.2f' forces to always show two decimals
    h_time = str(formula).split(".")
    return h_time

  if mins >= 60 and mins < 1440:
    h_time = Time()
    time = (f"{h_time[0]}h:{h_time[1]}m")
    return (time)
  elif mins >= 1440:
    h_time = Time()
    if int(h_time[0]) >= 24:
      h_time[0] = int(h_time[0])
      hours = int(h_time[0])
      formula = float((hours//24)+((hours//24)*(hours-24*(hours//24)))/(hours//24*100))
      formula = (f"{formula:.2f}")
      d_time = str(formula).split(".")
      time = (f"{d_time[0]}d:{d_time[1]}h:{h_time[1]}m")
      return (time)
  else:
    time = (f"{mins}m")
    return (time)

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