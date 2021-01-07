#from colored import fg
from os import popen
clear = popen('clear','r').read()
print(clear)

exp = input().split()
opt = []

for i in range(1,31):
  for x in range(2):
    exp[x] = float(exp[x])
    res = exp[x] * (2 ** i)
    if i==30:
      opt.append(res)
#print()
print(opt)