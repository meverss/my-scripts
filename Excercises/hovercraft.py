import os
os.system("clear")

hc = int(input())
hc_month = 10
hc_build_cost = 2000000
hc_price = 3000000
hc_insurance = 1000000
state = ''

goal = 10 * hc_price
invest = hc_build_cost * hc_month + hc_insurance
money = hc * hc_price

print(money)

if money <= (invest - 1):
  print('Loss')
elif money >= (invest + 1):
  print('Profit')
elif money == invest:
  print('Broke Even')



