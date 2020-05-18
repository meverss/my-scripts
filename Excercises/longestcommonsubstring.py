string = input().split(" ")
wlist = []
for a in range(len(string)):
  for i in string[a]:
    if i == i.upper() and string[a].index(i) != 0:
      string[a] = list(string[a])
      string[a].insert(string[a].index(i)," ")
      string[a] = ''.join(string[a])

string = ' '.join(string)
a_string = string.split(" ")

for x in range(len(a_string)):
  if string.count(a_string[x]) >= 2:
    wlist.append(a_string[x])

wlist.sort()
print(wlist[0])
