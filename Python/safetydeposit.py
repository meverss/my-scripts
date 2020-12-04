items = input().split(",")
item = input()

if item in items:
  print((items.index(item) + 1) * 5)
