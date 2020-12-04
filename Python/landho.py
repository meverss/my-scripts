from math import ceil as c
ahead = int(input())
trip = c((ahead + 1) / 20)
time = 0
if trip == 1:
 time = 10
else:
 time = trip * 20 - 10

print(time)