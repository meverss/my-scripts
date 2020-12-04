from datetime import datetime as dt
from calendar import month_name as m, day_name as d

date = (input()).title()
m = list(m)
d = list(d)

if "/" in date:
 date = date.split("/")
 new_date = dt(int(date[2]),int(date[0]),int(date[1]))
 print(d[new_date.weekday()])

elif "," in date:
  date = date.split()
  date[1] = (list(date[1]))
  date[1].remove(",")
  date[1] = ''.join(date[1])
  if date[0] in m:
    month = m.index(date[0])
    new_date = dt(int(date[2]),int(month),int(date[1]))
    print(d[new_date.weekday()])
