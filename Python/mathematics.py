result = int(input())
expr = input().split(" ")
check = ''

for a in expr:
  if eval(str(a)) == result:
    check = 'ok'
    break

if check == 'ok':
  print(f"index {expr.index(a)}")
else:
  print('none')