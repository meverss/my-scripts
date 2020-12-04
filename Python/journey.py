import os
os.system("clear")

#Journey from work to home:

distance = 20
print("Leaving work...")
while True:
  distance -= 2.5
  print(str(distance) + " Miles to get home...")
  if distance == 15:
    print("-- Stop at McDonalds")
    continue
  elif distance ==10:
    print("-- Short stop for some beers..")
    continue
  elif distance ==5:
    print("-- Sh...t! Have a flat tire!!")
    continue
  elif distance == 0:
    print("Finally home!!!")
    break