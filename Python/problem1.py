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
  
    