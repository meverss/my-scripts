text = input()
text = list(text [::-1])
chars = list('abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ ')
dword = ''

i = 0
while i <= (len(text) - 1):
  if text[i] in chars:
    dword += text[i]
  i += 1

#text = ''.join(text)
print(dword)
