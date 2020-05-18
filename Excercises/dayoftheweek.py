from datetime import datetime as dt

date = (input()).title()
m = ['January','February','March','April','May',\
    'June','July','August','September','October',\
    'November','December']

d = ['Monday','Tueaday','Wednesday','Thursday','Friday',\
    'Saturday','Sunday']

if "/" in date:
 date = date.split("/")
 new_date = dt(int(date[2]),int(date[0]),int(date[1]))
 print(d[new_date.weekday()])

elif "," in date:
  date = date.split(" ")
  date[1] = (list(date[1]))
  date[1].remove(",")
  date[1] = ''.join(date[1])
  if date[0] in m:
    month = m.index(date[0]) + 1
    new_date = dt(int(date[2]),int(month),int(date[1]))
    print(d[new_date.weekday()])
