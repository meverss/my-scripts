from decimal import Decimal, getcontext

num = int(input())
def pi():
  getcontext().prec=1000
  pi = (sum(1/Decimal(16)**k *
             (Decimal(4)/(8*k+1) -
              Decimal(2)/(8*k+4) -
              Decimal(1)/(8*k+5) -
              Decimal(1)/(8*k+6))
    for k in range(1000)))
  return pi

dec = str(pi()).split('.')
print(dec)
if 1000 > num > 0:
  print(dec[1][num-1])