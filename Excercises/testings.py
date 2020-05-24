from colored import fg, bg, attr
from os import system
clear = system("clear")

start = (f"{fg(48)}{attr(1)}")
path = (f"{fg(238)}")
end = (f"{fg(162)}{attr(1)}")
n = (f"{fg(250)}")
pos = 0
p = []
l = []
mymap = 'xxxxx,xpxxx,xxxxx,xpxxx,xxxxx'.upper()
smap = mymap.split(',')
sline = any(smap[x].count('P') == 1 for x in range(5))

for a in range(5):
  if sline == True:
    if 'P' not in smap[a] and pos != 0:
      smap[a] = list(smap[a])
      smap[a][p[0][1]] = f'{path}X{n}' if len(l) == 0 else f'{n}X'
      smap[a] = ''.join(smap[a])
      print(f"{n}{smap[a]}")

    elif 'P' in smap[a] and pos == 0:
      p.append([a,smap[a].index('P')])
      print(f"{n}"+smap[a].replace('P',f"{start}P{n}"))
      pos = 1

    elif 'P' in smap[a] and pos == 1:
      p.append([a,smap[a].index('P')])
      l.append(p[0][1])
      l.append(p[1][1])
      smap[a] = list(smap[a])
      if l[0] < l[1]:
        smap[a][l[0]] = f'{path}X'
      elif l[0] > l[1]:
        smap[a][l[1]+1] = f'{path}X'
        if l[0] < 4:
          smap[a][l[0]+1] = f'{n}X'
      smap[a] = ''.join(smap[a])
      print(smap[a].replace('P',f'{end}P{n}'))

    else:
      print(f"{n}{smap[a]}")

  elif sline == False:
    if 'P' in smap[a]:
      p.append(smap[a].index('P'))
      p.append(smap[a].rindex('P'))
      smap[a] = list(smap[a])
      smap[a][p[0]] = f'{start}P{path}'
      smap[a][p[1]] = f'{end}P{n}'
      smap[a] = ''.join(smap[a])
      print(smap[a])
    else:
      print(smap[a])
