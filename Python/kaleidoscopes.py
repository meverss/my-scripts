k = int(input())
sale = 0

if k > 1:
  sale = (k*5)-(10*5/100*k)
  tax = 7*sale/100
  sale += tax
else:
  sale = k*5
  tax = (7*sale/100)
  sale += tax
print(f{sale:.2f}")