blocks = input().upper() or "BBHBBP"
blocks = list(blocks)

h = blocks.index("H")
p = blocks.index("P")

if h > p:
  distance = h-p-1
elif p > h:
  distance = p-h-1

print(distance)