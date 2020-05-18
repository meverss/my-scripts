card = list(input())[::-1]
r_card = card

for a in range(len(r_card)):
  if a % 2 != 0:
    if int(r_card[a]) * 2 > 9:
      r_card[a] = int(r_card[a]) * 2 - 9
    else:
      r_card[a] = int(r_card[a]) * 2

for x in range(len(r_card)):
  r_card[x] = int(r_card[x])
print(r_card)
print(sum(r_card) % 2)
if len(card) == 16 and sum(r_card) % 2 == 0:
  print('valid')
else:
  print('not valid')