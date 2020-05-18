from itertools import permutations as perm
word = input().upper()
wlist = list(perm(word))

for a in range(len(wlist)):
  wlist[a] = ''.join(wlist[a])

wlist.sort()
wlist = set(wlist)
dlist = list(wlist.copy())
dlist.sort()

print(dlist.index(word) + 1)