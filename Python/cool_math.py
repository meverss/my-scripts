from colored import fg, bg, attr
from os import popen
clear = popen('clear','r').read()
print(clear)

red, ylw, normal = fg('red'), fg('yellow'), attr(0)

# Get screen size
size = list(int(x) for x in popen('stty size', 'r').read().split())

# Example 1
x = ''
for y in range(1,10):
  x += str(y)
  f = int(x)*8+y
  print((f"{x} x {red}8{normal} + {y} = {f}").center(size[1]+10))
print()

# Example 2
x = ''
for y in range(1,10):
  x += str(y)
  f = (int(x)*9+(y+1))
  print((f"{x} x 9 + {y+1} = {f}").center(size[1]))
print()

# Example 3
x = ''
for y in reversed(range(8)):
  x += str(y+2)
  f = int(x)*9+y
  print((f"{ylw}{x} x 9 + {y} = {f}{normal}").center(size[1]+13))
print()

# Example 4
x = ''
res = []
for y in range(1,10):
  x += '1'
  f = list(str(int(x)*int(x)))
  res.append(f)

for rslt in res:
  for num in range(1,10):
    for n,i in enumerate(rslt):
      if i == str(num):
        rslt[n] = f"{fg(240+num)}{rslt[n]}"
for x in range(len(res)):
  res[x] = ''.join(res[x])

q = ''
for i in range(len(res)):
  q += '1'
  print(f"{normal}{q} x {q} = ".rjust(size[1]//2+8) + f"{res[i]}")

