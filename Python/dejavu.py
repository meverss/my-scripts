text = input()
stat = ''

i=0
while i <= (len(text) - 2):
  if text[i] == text[i + 1]:
      stat = 'Deja Vu'
      break
  else:
      stat = 'Unique'
  i += 1
print(stat)
