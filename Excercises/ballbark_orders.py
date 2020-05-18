order = (input().title()).split(" ")
tax = 7
d_order = []
menu ={
    "Nachos":6,
    "Pizza":6,
    "Cheeseburger":10,
    "Water":4,
    "Coke":5
    }

for a in order:
  if a in menu:
    d_order.append(menu[a])
  elif a not in menu:
    d_order.append(menu["Coke"])

total = sum(d_order[x] for x in range(len(d_order))) 
total += 7 * total / 100
print(total)