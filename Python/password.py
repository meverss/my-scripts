from os import system
system("clear")

pwd = input()
import itertools  #Modulo para hacer combinaciones

nums = list(range(10))

chars = ('!', '@', '#', '$', '%', '&', '*')
nums = list(range(10))
strenght = ''

p_chars = list(itertools.combinations(chars, 2))
p_nums = list(itertools.combinations(nums, 2))

if len(pwd) <= 1:
  strenght = 'Weak'
else:
  for c in p_chars:
    if c[0] in list(pwd) and c[1] in list(pwd) or pwd.count(str(c[0])) >= 2 or pwd.count(str(c[1])) >= 2:
      next = True
    if next == True and len(pwd) >= 7:
      for n in p_nums:
        if str(n[0]) in list(pwd) and str(n[1]) in list(pwd) or pwd.count(str(n[0])) >= 2 or pwd.count(str(n[1])) >= 2:
          strenght = "Strong"
    else:
      strenght = 'Weak'

if strenght == 'Strong':
  print('Strong')
else:
  print('Weak')
