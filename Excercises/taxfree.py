prices = input().split(",")
total = 0
for a in range(len(prices)):
  prices[a] = float(prices[a])

for b in prices:
  if b < 20:
    b += b * 7 / 100
    total += b
  else:
    total += b

print(f"{total:.2f}")