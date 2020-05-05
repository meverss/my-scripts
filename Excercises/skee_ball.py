points = int(input())
squirt = int(input())

ticket = points // 12

if ticket >= squirt:
  print("Buy it!")
else:
  print("Try again")