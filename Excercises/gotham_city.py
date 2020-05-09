import os
os.system("clear")

criminals = int(input())

if criminals <= 4:
  print("I got this!")
elif criminals >= 5 and criminals <= 10:
  print("Help me Batman")
elif criminals >= 11:
  print("Good Luck out there!")
