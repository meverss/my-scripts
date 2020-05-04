num = int(input())
list_num = (range(1,num))
lenght = len(list_num)
sum = 0
print(lenght)
for i in list_num:
  if int(i) % 2 == 0:
    sum += i
  print(list_num[i-1])
  i += i
print(sum)