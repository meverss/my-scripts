numbers = input().split(" ")
for x in range(len(numbers)):
  numbers[x] = int(numbers[x])
nlist = []

for a in numbers:
  if a % 2 == 0:
    nlist.append(a)

for i in range(len(nlist)):
  nlist[i] = str(nlist[i])

nlist = ' '.join(nlist)

print(nlist)