from colored import fg
from os import popen
s = popen('clear && ls -h','r').read().split()
print(f"{fg('blue')}{s}")
print(len(s))
print(s[50])