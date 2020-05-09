import os
os.system("clear")

text = input()
text = list(text)
chars = list('abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890 ')
dword = ''

i = 0
while i <= (len(text) - 1):
  if text[i] in chars:
    dword += text[i]
  i += 1

print(dword)
