from string import digits
c_text = list(input())
d_text = ''

for a in range(len(c_text)):
  if c_text[a] in digits:
    char = c_text[a-1] * int(c_text[a])
    d_text += char

print(d_text)