text = list(input())
stat = ''

i=0
while i <= (len(text) - 2):
  if text[i] == text[i + 1]:
      stat = 'dejavu'
      break
  else:
      stat = 'unique'
  i += 1

if stat == 'unique':
  print('Unique')
elif stat == 'dejavu':
  print('Deja Vu')