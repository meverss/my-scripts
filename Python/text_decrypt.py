from random import randint as rnd
from string import digits as nums, punctuation as ch, ascii_letters as letters
from os import popen
clear = popen('clear','r').read()
print(clear)

txt_enc = input('Enter text: ')
chars = list(ch)
enc, dec, txt_dec, a = '',[],[],[]
let = list(letters) + chars
let.insert(14,'ñ')
let.insert(41,'Ñ')
let.append(' ')

# Decrypt:
decode = txt_enc.split('^%')
for a in decode:
  chk = any(x for x in a if x in letters or x in nums)
  if chk == True:
    dec.append(a)

for b in range(len(dec)):
  for c in range(len(dec[b])):
    if dec[b][c][0] != '-' and dec[b][c] not in nums and dec[b][c] not in letters:
      dec[b] = dec[b].replace(dec[b][c],'*')
  dec[b] = dec[b].replace('*','')

for x in range(len(dec)):
  while dec[x][-1] == '-':
    dec[x] = list(dec[x])
    dec[x] = dec[x][:-1]
    dec[x] = ''.join(dec[x])
  if dec[x][-1] in nums:
    txt_dec.append(let[int((int(dec[x])+5)/5)])
  elif dec[x][-1] in letters:
    txt_dec.append(str(let.index(dec[x])-22))
txt_dec = ''.join(txt_dec)

print(txt_dec)

