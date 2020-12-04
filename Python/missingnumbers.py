from string import digits as d
ll = int(input())
nlist = []
clist = []
for a in range(ll):
  n = int(input())
  nlist.append(n)
for x in range(nlist[0],nlist[-1]+1):
  clist.append(x)
for i in nlist:
  if i in clist:
    clist.remove(i)
for n in range(len(clist)):
  clist[n] = str(clist[n])
clist = ' '.join(clist)
print(clist)