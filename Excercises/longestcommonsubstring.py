import re
string = input('Enter list: ').split(" ")
plist = []
sp = ''
length = []

## Seek for the longest length
for ml in string:
  length.append(len(ml))
maxlen = max(length)

## Create a list with all patterns
for x in range(maxlen):
  for a in range(len(string)):
    for i in string[a][x::]:
      if all(re.search(sp,ind) for ind in string):
        if sp != '':
          plist.append(f"{sp}")
      sp += i
    sp = ''

## Seek for the Longest Common Substring
plist = list(set(plist))
plist.sort(key=len, reverse=True)
pattern = plist[0]

print(plist)
