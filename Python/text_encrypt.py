from random import randint as rnd
from string import digits as nums, punctuation as ch, ascii_letters as letters
from os import popen
clear = popen('clear','r').read()
print(clear)

t = list(input('Enter text: '))
chars = list(ch)
enc, dec, txt_dec, a = '',[],[],[]
let = list(letters) + chars
let.insert(14,'ñ')
let.insert(41,'Ñ')
let.append(' ')

# Encrypt:
for x, item in enumerate(t):
  if item in let:
    t[x] = list('^' + str(let.index(item)*5-5))
    for q in range(1,len(t[x])):
      t[x][q] = '%' + t[x][q]
    t[x] = ''.join(t[x])
  elif item in nums:
    t[x] = '^%' + let[int(item)+22]
for i in range(len(t)*2):
  t.insert(rnd(0,len(t)-1),chars[rnd(0,len(chars)-1)])
txt_enc = ''.join(t)

print(txt_enc)

