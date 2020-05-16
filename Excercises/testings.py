from os import system
from shutil import get_terminal_size as ts
print('{:^61}'.format("Marvin Eversley Silva"))
text = 'MarvincEversley Silva'
#cols = int(system("echo $COLUMNS"))
cols = ts()
print(cols[0])
#print(f"{text:{cols}}")