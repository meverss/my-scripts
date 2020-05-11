from colors import color
import os

os.system("clear")
i=0
while i <= 255:
  print(color(str(i) + " - Marvin Eversley Silva",fg=i,style='faint'))
  i += 1 