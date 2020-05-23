num = int(input())
lnum = filter(lambda a: a % 3 == 0 or a % 5 == 0,range(num))
pnum = []
for a in lnum:
  pnum.append(a)
print(sum(pnum))