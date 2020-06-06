t = int(input() or 1)
odds = []
i=1
if 1 <= t <= 100:
  while i <= t:
    num = int(input() or 5)
    if 1 <= num <= 1000:
      alist = list(range(1,num + 1))
#      print(alist)
      for n in alist:
#        print(n)
#        print(list(n%x for x in alist if x != n))
        o = list(n%x ==0 for x in alist if x != n)
#        print(o)
        if o.count(True) % 2 != 0:
          odds.append(n)
#          print(odds)
      print(len(odds))
      odds = []
    i += 1