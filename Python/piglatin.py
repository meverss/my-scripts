import os
os.system("clear")

english = ((input('English: ')))
piglatin = ''
pl_word = ''

# translate
words = list(english.split(" "))
i = 0
while i <= (len(words)) - 1:
  new_w = list(words[i])
  new_w.append(words[i][0])
  new_w.remove(words[i][0])
  pl_word = ''.join(new_w)+'ay '
  piglatin += pl_word
  i += 1
print(piglatin)
