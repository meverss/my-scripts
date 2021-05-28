#from colored import fg
from os import popen
clear = popen('clear','r').read()
print(clear)

exp = float(input())#.split('$')

for i in range(1,31):
#    exp[1] = float(exp[1])
    res = exp * (2 ** i)
print(res)
