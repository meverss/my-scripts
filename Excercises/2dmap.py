map2d = (input().upper()).split(',')

cidx = []
ridx = []
mode = 0

for a in range(len(map2d)):
  if 'P' in map2d[a]:
    if map2d[a].count('P') == 1:
      cidx.append(map2d[a].index('P'))
      ridx.append(a)
      mode = 0
    elif map2d[a].count('P') == 2:
      cidx.append(map2d[a].index('P'))
      cidx.append(map2d[a].rindex('P'))
      mode = 1

if mode == 0:
  cidx.sort()
  ridx.sort()
  p1 = cidx[1] - cidx[0]
  p2 = ridx[1] - ridx[0]
  steps = p2 + p1
elif mode == 1:
  steps = cidx[1] - cidx[0]

print(steps)

