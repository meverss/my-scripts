"""
Title:    2D Map
Author:   MeVeRsS

Description:
In a representation of a 5x5 2D map, and if you can only move left, right, up, or down, determine how many moves are needed to get between two points.

The points that you move between are marked with a P and the spaces in between are marked with X.

Sample Input:
XPXXX,XXXXX,XXXXX,XXXPX,XXXXX
"""
from colored import fg, attr
from os import system
clear = system("clear")

start = (f"{fg(48)}{attr(1)}")
path = (f"{fg(238)}")
end = (f"{fg(162)}{attr(1)}")
n = (f"{fg(250)}")
cidx = []
ridx = []

map2d = input() or 'XPXXX,XXXXX,XXXXX,XXXPX,XXXXX'.upper()

## DRAW MAP
class MyMap():

  def __init__(self, mymap):
    self.mymap = mymap

  def drawmap(mymap):
    pos = 0
    p = []
    l = []
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

  def steps(mymap):
    mymap = mymap.split(',')
    print(mymap)
    for a in range(5):
      if 'P' in mymap[a]:
        if mymap[a].count('P') == 1:
          cidx.append(mymap[a].index('P'))
          ridx.append(a)
          mode = 0
        elif mymap[a].count('P') == 2:
          cidx.append(mymap[a].index('P'))
          cidx.append(mymap[a].rindex('P'))
          mode = 1

    if mode == 0:
      cidx.sort()
      ridx.sort()
      p1 = cidx[1] - cidx[0]
      p2 = ridx[1] - ridx[0]
      steps = p2 + p1
    elif mode == 1:
      steps = cidx[1] - cidx[0]

    return steps
#================================
print(f"Done in {MyMap.steps(map2d)} steps.")
MyMap.drawmap(map2d)