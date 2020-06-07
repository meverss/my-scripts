from string import ascii_lowercase as low
num = int(input())
if 1 <= num <= 26:
  low = list(low[x] for x in range(len(low))[:num])
  low = ''.join(low[::-1])
print(low)