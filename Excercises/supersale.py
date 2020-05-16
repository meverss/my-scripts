prices = input().split(",")

item_dis = 0
discount = 0
total_items_dis = 0
tax = 0

for i in range(len(prices)):
  prices[i] = float(prices[i])
prices.sort()
o_prices = prices[::-1]

for a in range(1,len(prices)):
  item_dis = o_prices[a] - (30 * float(o_prices[a]) / 100)
  total_items_dis += item_dis

total_no_tax = o_prices[0] + total_items_dis
save_no_tax = sum(o_prices[x] for x in range(len(o_prices))) - total_no_tax

tax = 7 * save_no_tax / 100

save_with_tax = save_no_tax + tax

print(int(save_with_tax))