"""
In this secuence, what's the missing number?

1 + 4 = 5
2 + 5 = 12                                              3 + 6 = 21                                              4 + 7 = 32
5 + 8 = 45                                              6 + 9 = 60
8 + 11 = ?

"""

import os
os.system("clear")

a = [5]
for x in range(1,9): 
  calc = f'{x} + {x + 3}'
  res = eval(calc)
  if x == 1:
    print(f'{calc} = {res}')
  else:
    print(f'{calc} = {res + a[x-2]}')
    a.append(res + a[x-2])
    