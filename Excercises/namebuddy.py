group = (input().title()).split(" ")
v = 0
myname = input().title()

for a in group:
  if myname[0] == a[0]:
    v = 1
    break
  else:
    v = 0

if v == 1:
  print('Compare notes')
elif v == 0:
  print('No such luck')