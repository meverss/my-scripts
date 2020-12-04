string = input()
v = 'aeiouAEIOU'
vowels = filter(lambda x: x in v,string)
vlist = ''
for x in vowels:
  vlist += x
print(len(vlist))

