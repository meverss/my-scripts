text = input()
alien_text = text.split(" ")

for i in alien_text:
  tr_txt = i [::-1]
  alien_text[alien_text.index(i)] = tr_txt

alien_text = ' '.join(alien_text)
print(alien_text)