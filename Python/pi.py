from decimal import Decimal, getcontext

def pi():
  getcontext().prec=1000

  pi = (sum(1/Decimal(16)**k *
    (Decimal(4)/(8*k+1) -
    Decimal(2)/(8*k+4) -
    Decimal(1)/(8*k+5) -
    Decimal(1)/(8*k+6))
    for k in range(1000)))
  return pi

print(pi())
input("Pulse la teclita 'Enter'")