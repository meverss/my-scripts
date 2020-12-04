rrund = int(input())
rruns = int(input())
coysp = int(input())

rtts = rrund / rruns
ctts = (rrund + 50) / (coysp)

if rtts < ctts:
  print('Meep Meep')
else:
  print('Yum')
