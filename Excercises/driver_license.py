name = input()
name = name.title()
agents = int(input())
others = input()
cue = name + " " + others
cue = cue.title()
cue = cue.split(" ")
cue.sort()
my_turn = int((cue.index(name))+1)

import math

if my_turn >= agents:
  rnd = math.ceil(my_turn / agents)
  license = rnd * 20
else:
  license = 20

print(license)