from colored import fg, attr
cT = fg(48)
cF = fg('red')
codd = fg('yellow')
nc = attr(0)

t = int(input() or 1)
check = ''
odds = []
lodds = []
i=1
if 1 <= t <= 100:
  while i <= t:
    num = int(input() or 5)
    if 1 <= num <= 1000:
      alist = list(range(1,num + 1))
      for n in alist:
        o = list(n % x == 0 for x in alist if x != n)
## --------------------------------
#        co = o.copy()
#        for x in range(len(co)):
#          co[x] = f'{cF}{str(co[x])}{nc}' if co[x] == False else f'{cT}{co[x]}{nc}'
#          check += f'{co[x]} '
#        isodd = f'{codd}({o.count(True)}){nc}' if o.count(True) % 2 != 0 else f'{nc}({o.count(True)})'
#        print(n)
#        print(f'{check} {isodd}')
#        check = ''
## --------------------------------
        if o.count(True) % 2 != 0:
          odds.append(n)
      lodds.append(len(odds))
      odds = []
    i += 1
for x in lodds:
  print(x)