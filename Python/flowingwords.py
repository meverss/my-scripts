string = input().split(" ")

if all(string[a][0] == string[a-1][-1] for a in range(1,len(string)-1)):
  print('true')
else:
  print('false')