from os import system
from random import shuffle

clear = system("clear")
clear

row = []
sudoku = []
box = []
i = 0
while i <= 8:
  rng = [1,2,3,4,5,6,7,8,9]
  row.append(f"{rng[0:3]},{rng[3:6]},{rng[6:]}")
  sudoku.append(row)
  row = []
  i += 1

block0 = list(f"{sudoku[0][0][0]} {sudoku[0][0][1]} {sudoku[0][0][2]} \
            {sudoku[1][0][0]} {sudoku[1][0][1]} {sudoku[1][0][2]} \
            {sudoku[2][0][0]} {sudoku[2][0][1]} {sudoku[2][0][2]}").split(" ")

rng = []
for i in range(1,10):
  rng.append(i)

def check1():
#  bl1 = (f"{sudoku[0][0][0]} {sudoku[0][0][1]} {sudoku[0][0][2]} \
#           {sudoku[1][0][0]} {sudoku[1][0][1]} {sudoku[1][0][2]} \
#           {sudoku[2][0][0]} {sudoku[2][0][1]} {sudoku[2][0][2]}").split(" ")

  ch = all(i in rng for i in block0)
#  print(f"1 {bl1}\ch {ch}")
  if ch == True:
    print(f"Este: {ch}")
    return True
  else:
    return False


print(check1())

while check1() == True:
#  sudoku[0][0].split(",")
  shuffle(sudoku[0][0])
#  shuffle(sudoku[1])
#  shuffle(sudoku[2])
#  sudoku[0][0] + sudoku[0][1] + sudoku[0][2] + sudoku[1][0] + sudoku[1][1] + sudoku[1][2] + sudoku[2][0] + sudoku[2][1] + sudoku[2][2]
#  check1()
  print(sudoku[0][0])
#### PRINT SUDOKU

for a in sudoku:
  print(a)
