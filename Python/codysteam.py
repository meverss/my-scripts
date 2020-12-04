num = input().split()
num = list(int(n) for n in num)
stu = input().split()
stu = list(int(s) for s in stu)
stu.append(min(stu)-1)
grps = []
sgrp = []
kcsum = []

if 1 <= len(stu) <= num[0]+1:
  for x in range(len(stu)):
    if stu[x] is not stu[-1]:
      if stu[x] < stu[x+1] or (stu[x] > stu[x-1] and x != 0):
        sgrp.append(stu[x])
        if stu[x] > stu[x+1]:
          grps.append(sgrp)
          sgrp = []

  if num[1] > 1:
    grps = list(filter(lambda x: len(x) >= num[1], grps))
    print(grps)
    for k in grps:
      for n in range(len(k)-(num[1]-1)):
        print(k[n:n+num[1]])
        kcsum.append(sum(k[n:n+num[1]]))
      print(max(kcsum))
  else:
    print(max(stu))

