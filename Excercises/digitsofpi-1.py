from math import pi

num = int(input())
def mypi():
  getcontext().prec=1000
  mypi = (sum(1/Decimal(16)**k *
    (Decimal(4)/(8*k+1) -
    Decimal(2)/(8*k+4) -
    Decimal(1)/(8*k+5) -
    Decimal(1)/(8*k+6))
    for k in range(1000)))
  return mypi

dec = (pi)#.split('.')
print(f'{dec:.1000f}')
#if 1000 > num > 0:
#  print(dec[1][num-1])