number = int(input())
nlist = input().split(" ")
for a in range(len(nlist)):
  nlist[a] = int(nlist[a])

if all(number % x == 0 for x in nlist):
  print('divisible by all')
else:
  print('not divisible by all')
