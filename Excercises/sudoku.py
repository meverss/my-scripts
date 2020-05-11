from os import system
from random import shuffle

clear = system("clear")
clear

sudoku = []
row  = ''

#rng = []
#for i in range(1,10):
#  rng.append(i)

i = 0
while i <= 8:
  rng = str(123456789)
#  row = (rng[0:3] +  rng[3:6] +  rng[6:])#.split(" ")
  row = (f"{rng[0:3]} {rng[3:6]} {rng[6:]}").split(" ")

  r = 0
  while r <= 2:
    row[r] = list(row[r])
    r += 1
  shuffle(row)
  sudoku.append(row)
  print(int(row[0][0]) + int(row[0][1]) + int(row[0][2]))
  i += 1

block0 = (f"{sudoku[0][0][0]} {sudoku[0][0][1]} {sudoku[0][0][2]} \
            {sudoku[1][0][0]} {sudoku[1][0][1]} {sudoku[1][0][2]} \
            {sudoku[2][0][0]} {sudoku[2][0][1]} {sudoku[2][0][2]}").split(" ")

#print(block0)

def check1():
  if any(x in rng for x in block0):
    return True
  else:
    return False

print(check1())

while check1() == True:
  shuffle(sudoku[0])
#  shuffle(sudoku[1])
#  shuffle(sudoku[2])
#  sudoku[0][0] + sudoku[0][1] + sudoku[0][2] + sudoku[1][0] + sudoku[1][1] + sudoku[1][2] + sudoku[2][0] + sudoku[2][1] + sudoku[2][2]
#  check1()
  print(sudoku[0])
#### PRINT SUDOKU

for a in sudoku:
  print(a)
