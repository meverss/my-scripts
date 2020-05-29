import os
os.system("clear")

date = (input()).title()
m = ['January','February','March','April','May',\
    'June','July','August','September','October',\
    'November','December']

if "/" in date:
 date = date.split("/")
 eu = (f"{str(date[1])}/{str(date[0])}/{str(date[2])}")
 print(eu)

elif "," in date:
  date = date.split(" ")
  date[1] = (list(date[1]))
  date[1].remove(",")
  date[1] = ''.join(date[1])
  if date[0] in m:
    month = m.index(date[0]) + 1
    eu = (f"{str(date[1])}/{str(month)}/{str(date[2])}")
    print(eu)


