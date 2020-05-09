import os
os.system("clear")

time = input()
time = time.upper()
time = time.split(":")

if "PM" in time[1] and int(time[0]) <= 11:
  H = int(time[0]) + 12
  HH = str(H) + ":" + str(time[1][0]) + str(time[1][1])
  print(HH)
elif int(time[0]) == 12  and "AM" in time[1]:
  H = '00'
  HH = str(H) + ":" + str(time[1][0]) + str(time[1][1])
  print(HH)
elif int(time[0]) <= 12  and "AM" in time[1]:
  if int(time[0]) <= 9:
    H = "0" + str(int(time[0]))
  else:
    H = time[0]
  HH = str(H) + ":" + str(time[1][0]) + str(time[1][1])
  print(HH)
elif int(time[0]) == 12  and "PM" in time[1]:
  H = time[0]
  HH = str(H) + ":" + str(time[1][0]) + str(time[1][1])
  print(HH)