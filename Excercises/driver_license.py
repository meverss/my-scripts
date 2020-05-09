import os
os.system("clear")
print("Driving License \nAuthor: MeVeRsS\n")
name = (input("¿Cuál es tu nombre? ")).title()
try:
  agents = int(input("¿Cuántos agentes hay trabajando? "))
except ValueError:
  print("Debe introducir un número entero")
others = input("¿Quien más está en la cola? ")
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
print("Vas en la " + str(rnd) + " vuelta, así que tu licencia estará en " + str(license) + " min.")
