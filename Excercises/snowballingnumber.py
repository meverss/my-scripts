numbers = int(input())
nlist = []
for n in range(numbers):
  q = int(input())
  nlist.append(q)
for a in range(len(nlist)):
  nlist[a] = int(nlist[a])
if all(nlist[x] > sum(nlist[:x]) for x in range(1,len(nlist))):
  print('true')
else:
  print('false')