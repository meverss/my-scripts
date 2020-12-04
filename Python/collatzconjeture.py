"""
Title:	Collatz Conjecture
Script:	MeVeRsS

Description:
The Collatz conjecture (also known as the Ulam
conjecture or the Syracuse problem) is an unsolved
 mathematical problem, which is very easy to formulate:

1. Take any natural number
2. If it's even, half it, otherwise triple it and add one
3. Repeat step 2. until you reach 4, 2, 1 sequence
4. You will ALWAYS reach 1, eventually.
"""


num = int(input('Enter a number: '))
x = num
cnt = 0

while x != 1:
  if x % 2 == 0:
    print(f"{int(x)} / 2 = {int(x / 2)}")
    x /= 2
    cnt += 1
  else:
    print(f"{int(x)} * 3 + 1 = {int(x * 3 + 1)}")
    x = x * 3 + 1
    cnt +=1
  if x == 1:
    print(f"\nIt took {cnt} iterations for x to converge to 1.")
