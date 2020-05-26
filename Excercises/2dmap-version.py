"""
Title:    2D Map
Author:   MeVeRsS

Description:
In a representation of a 5x5 2D map, and if you can only move left, right, up, or down, determine how many moves are needed to get between two points.

The points that you move between are marked with a P and the spaces in between are marked with X.

Sample Input:
XPXXX,XXXXX,XXXXX,XXXPX,XXXXX (Without spaces)
"""
from os import system
clear = system("clear")

cidx = []
ridx = []

map2d = input('Draw your map: ').upper() or 'XPXXX,XXXXX,XXXXX,XXXPX,XXXXX'.upper()

class MyMap():

  def __init__(self, mymap):
    self.mymap = mymap

  def drawmap(mymap):
    pos = 0
    p = []
    l = []
    smap = mymap.split(',')
    sline = any(smap[x].count('P') == 1 for x in range(5))

    print()
    for a in range(5):
      if sline == True:
        if 'P' not in smap[a] and pos != 0:
          smap[a] = list(smap[a])
          smap[a][p[0][1]] = f'⬜'if len(l) == 0 else '⬛'
          smap[a] = ''.join(smap[a])
          print(smap[a].replace('X','⬛'))

        elif 'P' in smap[a] and pos == 0:
          p.append([a,smap[a].index('P')])
          print(smap[a].replace('P',"🅰️").replace('X','⬛'))
          pos = 1

        elif 'P' in smap[a] and pos == 1:
          p.append([a,smap[a].index('P')])
          l.append(p[0][1])
          l.append(p[1][1])
          smap[a] = list(smap[a])
          if l[0] < l[1]:
            smap[a][l[0]:l[1]] = '⬜'*(l[1]-l[0])
          elif l[0] > l[1]:
            smap[a][l[1]+1:l[0]+1] = '⬜'*(l[0]-l[1])
            if l[0] < 4:
              smap[a][l[1]+1:l[0]+1] = '⬜'*(l[0]-l[1])
          smap[a] = ''.join(smap[a])
          print(smap[a].replace('P','🅱️').replace('X','⬛'))

        else:
          print(smap[a].replace('X','⬛'))

      elif sline == False:
        if 'P' in smap[a]:
          p.append(smap[a].index('P'))
          p.append(smap[a].rindex('P'))
          smap[a] = list(smap[a])
          smap[a][p[0]] = '🅰️'
          smap[a][p[0]+1:p[1]+1] = '⬜'*(p[1]-p[0])
          smap[a][p[1]] = '🅱️'
          smap[a] = ''.join(smap[a])
          print(smap[a].replace('X','⬛'))
        else:
          print(smap[a].replace('X','⬛'))

    print(f'\nLEGEND:')
    print(f"🅰️ - Start point.")
    print(f"🅱️ - End point.")
    print(f"⬜ - Choosen path (Same steps no matter which path you choose)")

  def steps(mymap):
    mymap = mymap.split(',')
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

print(map2d)
MyMap.drawmap(map2d)
print(f"\nWent from 🅰️ to 🅱️ in {MyMap.steps(map2d)} steps.")
