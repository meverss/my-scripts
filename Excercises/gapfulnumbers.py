try:
  num = int(input('Enter an integer number: '))
  num = str(num)
  if len(num) >= 3:
    if int(num) % int(f'{num[0]}{num[-1]}') == 0:
      print(f'{num} is a Gapful number cause it\'s divisible by {num[0] + num[-1]}')
    else:
      print(f'{num} is NOT a Gapful Number cause it\'s NOT divisible by {num[0] + num[-1]}')
  else:
    print('It most have at least 3 digits')
    exec(open(__file__).read())
except ValueError:
  print(f'Your input is not even a number. Try again.')
  exec(open(__file__).read())