prices_eur = input().split(" ")
prices_usd = []
back_to_store = ''
for a in prices_eur:
  prices_usd.append(f"{float(a) * 1.1:.2f}")

for i in prices_usd:
  if float(i) > 20:
    back_to_store = 'True'
    break
  else:
    back_to_store = 'False'

if back_to_store == 'True':
  print('Back to the store')
elif back_to_store == 'False':
 print('On to the terminal')