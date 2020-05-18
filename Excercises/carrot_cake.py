carrots = int(input())
boxes = int(input())

cfc = carrots % boxes

if cfc >= 7:
  print("Cake Time")
else:
  print(f"We need to buy {7 - cfc} more")