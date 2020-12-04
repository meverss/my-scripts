import os
os.system("clear")

phrase = input()
num = list(range(11))
new_phrase = list(phrase)

def numbers(i):
  switcher={
	  0:'zero',
	  1:'one',
	  2:'two',
	  3:'three',
	  4:'four',
	  5:'five',
	  6:'six',
	  7:'seven',
	  8:'eight',
	  9:'nine',
	  10:'ten'
	  }
  return switcher.get(i,"Invalid number")

i = 0

while i <= (len(num) - 1):
  if str(num[i]) in new_phrase:
    n = str(num[i])
    new_phrase[new_phrase.index(n)] = numbers(i)

  i += 1

new_phrase = ''.join(new_phrase)

if "onezero" in new_phrase:
  new_phrase = new_phrase.split(" ")
  new_phrase[new_phrase.index("onezero")] = "ten"
  new_phrase = ' '.join(new_phrase)

print(new_phrase)
