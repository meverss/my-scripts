from calendar import monthrange as mr, month_name as mn
days = 0

s_date = (input().title()).split(" ")
e_date = (input().title()).split(" ")

def conv_date(date):
  month = []
  for i in mn:
    month.append(i)
  month.remove('')

  date[1] = (list(date[1]))
  date[1].remove(",")
  date[1] = ''.join(date[1])
  if date[0] in month:
    m = month.index(date[0]) + 1
    new_date = (int(date[1]),int(m),int(date[2]))
  return new_date

ss_date = (conv_date(s_date))
ee_date = (conv_date(e_date))
s_year = int(ss_date[2])
s_month = int(ss_date[1])
s_days = int(ss_date[0])
e_year = int(ee_date[2])
e_month = int(ee_date[1])
e_days = int(ee_date[0])

if s_year != e_year:
  for y in range(s_year + 1, e_year):
    if y % 4 == 0:
      days += 366
    else:
      days += 365

  for m in range(s_month+1,13):
    d = mr(s_year, m)
    days += d[1]
  days += (mr(s_year,s_month)[1] - s_days)

  for m in range(1,e_month):
    d = mr(e_year, m)
    days += d[1]

  days += e_days
print(days)