t = int(input() or 1)
res = []
i=1
if 1 <= t <= 10:
  while i <= t:
    marks = input().split() or '75 55'.split()
    ok = all(1 <= int(marks[x]) <= 100 for x in range(len(marks)))
    if int(marks[0]) > 70 and int(marks[1]) > 50 and ok:
      res.append('Pass')
    else:
      res.append('Fail')
    i += 1
for x in res:
  print(x)