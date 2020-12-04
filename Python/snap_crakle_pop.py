rinbowls = []
sound = ''
sounds = []

a = 1
while a <= 6:
 bowl = input()
 rinbowls.append(bowl)
 a += 1
print(rinbowls)

for i in rinbowls:
  if int(i) % 3 == 0:
    sound = 'Pop'
    sounds.append(sound)
  elif int(i) % 3 != 0 and int(i) % 2 != 0:
    sound = 'Snap'
    sounds.append(sound)
  elif int(i) % 3 != 0 and int(i) % 2 == 0:
    sound = 'Crakle'
    sounds.append(sound)

sounds = " ".join(sounds)
print(sounds)