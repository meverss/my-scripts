num = int(input())
def Q(n):
  x = 0
  x = (num-Q(n-1))+Q(x-Q(x-2))
  return x

print(Q(num))