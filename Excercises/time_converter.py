"""
Title:        time_converter
Author:       MeVeRs
Description:
This code converts time in minutes into hours and minutes
format (h:m)
"""

from os import system
#from colored import fg, bg, attr

cls = system("clear")

m = int(input("Enter time in minutes: "))

def convert(mins):
  def Time():
    formula = float(((mins//60)+((mins//60)*(mins-60*(mins//60)))/(mins//60*100)))
    formula = (f"{formula:.2f}") ## Here '.2f' turns it into a float end adds 2 decimals
    h_time = str(formula).split(".")
    return h_time

  if mins >= 60 and mins < 1440:
#    Time()
    h_time = Time()
    time = (f"{h_time[0]}h:{h_time[1]}m")
    return (time)
  elif mins >= 1440:
    h_time = Time()
    if int(h_time[0]) >= 24:
      h_time[0] = int(h_time[0])
      hours = int(h_time[0])
      formula = float(((hours//24)+((hours//24)*(hours-24*(hours//24)))/(hours//24*100)))
      formula = (f"{formula:.2f}")
      d_time = str(formula).split(".")
      time = (f"{d_time[0]}d:{d_time[1]}h:{h_time[1]}m")
    return (time)
  else:
    time = (f"{mins}m")
    return (time)

print(convert(m))