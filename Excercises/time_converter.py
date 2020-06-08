"""
Title:        Time Converter
Author:       MeVeRs
Description:
This code converts time in minutes into hours and minutes
format (h:m)
"""

from os import system
from colored import fg, bg, attr
from functools import lru_cache as cache

clear = system("clear")

## COLORS
question = (f"{fg(130)}")
error = (f"{fg(125)}")
normal = (f"{attr(0)}")

def convert(minutes):
  @cache(10)
  def base_time():
    formula = float((minutes//60)+((minutes//60)*(minutes-60*(minutes//60)))/(minutes//60*100))
    formula = (f"{formula:.2f}")
    h_base_time = str(formula).split(".")
    return h_base_time

  if minutes >= 60 and minutes < 1440:
    h_base_time = base_time()
    base_time = (f"{h_base_time[0]}h:{h_base_time[1]}m")
    return (base_time)
  elif minutes >= 1440:
    h_base_time = base_time()
    if int(h_base_time[0]) >= 24:
      h_base_time[0] = int(h_base_time[0])
      hours = int(h_base_time[0])
      formula = float((hours//24)+((hours//24)*(hours-24*(hours//24)))/(hours//24*100))
      formula = (f"{formula:.2f}")
      d_base_time = str(formula).split(".")
      time = (f"{d_base_time[0]}d:{d_base_time[1]}h:{h_base_time[1]}m")
      return (time)
  else:
    time = (f"{minutes}m")
    return (time)

if __name__ == '__main__':

  try:
    m = int(input(f"{question}Enter time in minutes: {normal}"))
    print(convert(m))
  except ValueError:
    print(f"{error}Type an integer value{normal}")
    system("sleep 2")
    exec(open(__file__).read())