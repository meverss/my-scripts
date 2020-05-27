string = input().split(' ')
for a in string:
  print(f"{a}:{string.count(a)}")