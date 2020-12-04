import os
os.system("clear")

lenght = int(input())
list = 0
i = 1
while i <= lenght:
  a = int(input())
  if a % 2 == 0:
    list += a
  i += 1
print(list)