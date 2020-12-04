from math import sqrt
t = int(input() or 1)
sqr = []
i=1
if 1 <= t <= 100:
  while i <= t:
    num = int(input() or 4)
    if 1 <= num <= 10**9:
      sqr.append(round(sqrt(num)))
    i += 1
for x in sqr:
  print(x)