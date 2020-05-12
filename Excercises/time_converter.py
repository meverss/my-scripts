from os import system
from colored import fg, bg, attr
clear = system("clear")

m = int(input("Enter time in minutes: "))

def convert(mins):
  if mins >= 60:
    formula = float(((mins//60)+((mins//60)*(mins-60*(mins//60)))/(mins//60*100)))
    formula = (f"{formula:.2f}") ## Here '.2f' hurns it into a float end adds 2 decimals
    s_time = str(formula).split(".")
    time = (f"{s_time[0]}h:{s_time[1]}m")

    return print(time)
  else:
    time = (f"{mins}m")
    return print(time)

convert(m)