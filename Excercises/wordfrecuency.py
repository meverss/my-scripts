num = int(input())
string = input().split()
vword = all(1 <= len(string[w]) <= 40 for w in range(len(string)))

if len(string) <= num < 20 and vword:
  s = string.copy()
  s.sort(key=(lambda x: string.count(x)), reverse = True)
  i = []
  s = list(dict.fromkeys(s).keys())
  s = ' '.join(s)
  print(s)


#['blue', 'blue', 'blue', 'green', 'green', 'red', 'red', 'pink']
#blue blue blue green green red red pink