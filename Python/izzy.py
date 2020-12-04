snack = (input().title()).split(" ")
izzy = 0
menu = {
     "Lettuce": 5,
     "Carrot": 4,
     "Mango": 9,
     "Cheeseburger": 0
     }

for a in snack:
  if a in menu:
    izzy += menu[a]

if izzy >= 10:
  print('Come on Down!')
else:
  print('Time to wait')