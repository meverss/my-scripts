import os
os.system("clear")

snd={
    "Grr":"Lion",
    "Rawr":"Tiger",
    "Ssss":"Snake",
    "Chirp":"Bird"
    }

wsuh=(input().title()).split(" ")
animals = []

for a in wsuh:
  if a in snd:
    print(snd.get(a))
    animals.append(snd.get(a))

animals=' '.join(animals)
print(animals)
