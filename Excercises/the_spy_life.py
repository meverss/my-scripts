import os
os.system("clear")

from string import punctuation as symbols, digits

text = input()
text = text [::-1]
text = list(text)

i = 0
while i <= len(text) - 1:
  for a in text:
    if a in symbols or a in digits:
      text.remove(a)
  i += 1

text = ''.join(text)
print(text)
