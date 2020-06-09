import re
string = input('Enter list: ').split(" ")
plist = []
sp = ''

## Seek for the longest length
length = list(len(string[x]) for x in range(len(string)))
length = [int(length[x]) for x in range(len(length))]
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
plist = list(dict.fromkeys(plist).keys())
plist.sort(key=len, reverse=True)

print(plist[0]) if len(plist) > 0 else print('No longest common pattern found.')
