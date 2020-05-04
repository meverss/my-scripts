essay = input()
signs = [".", ",", ";", ":", '"','?','!','','','','','']
words = essay

import math  #Modulo de matematica. < math.ceil() > para redobdear..

for i in signs:
  words = words.split(i)
  words = ''.join(words)
words = words.split(" ")

print(len(words))
lenghts = 0

for l in words:
  lenghts += len(l)

average = (math.ceil(lenghts / len(words)))

print(words)
print(average)



