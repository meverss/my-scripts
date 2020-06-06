n = int(input() or 6)
array = input().split() or '1 2 3 4 10 12'.split()
if len(array) == n:
  asum = sum(list(int(array[x]) for x in range(n)))
  print(asum)
