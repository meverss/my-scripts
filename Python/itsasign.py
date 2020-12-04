a = 1
words = []
openb = ''
while a <= 4:
  word = input()
  words.append(word)
  a += 1

for i in words:
  if i == i[::-1]:
    openb = 'yes'
    break

if openb == 'yes':
  print('Open')
else:
  print('Trash')