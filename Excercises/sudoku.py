from os import system
from random import shuffle

clear = system("clear")
clear

sudoku = []
row  = ''

class Sudoku():

  def check1():

    i = 0
    while i <= 8:
      rnd = str(123456789)
      row = (f"{rnd[0:3]} {rnd[3:6]} {rnd[6:]}").split(" ")



      r = 0
      while r <= 2:
        row[r] = list(row[r])
        r += 1
      shuffle(row)
      sudoku.append(row)
      i += 1

    block0 = (f"{sudoku[0][0][0]} {sudoku[0][0][1]} {sudoku[0][0][2]} \
                {sudoku[1][0][0]} {sudoku[1][0][1]} {sudoku[1][0][2]} \
                {sudoku[2][0][0]} {sudoku[2][0][1]} {sudoku[2][0][2]}").split(" ")

    if all(x in block0 for x in rnd):
      return True
    else:
      for a in row:
        print(a)
        print()
      return False

while Sudoku.check1() == False:
#  row[0]=list(''.join(row[0]))
#  shuffle(row[0][0])
  print(Sudoku.check1())
#  shuffle(sudoku[0])
#  shuffle(sudoku[1])
#  shuffle(sudoku[2])
#  sudoku[0][0] + sudoku[0][1] + sudoku[0][2] + sudoku[1][0] + sudoku[1][1] + sudoku[1][2] + sudoku[2][0] + sudoku[2][1] + sudoku[2][2]

#  print(row[0])
#  print(row[1])
#  print(row[2])
#  print()

  system("sleep 2")
  Sudoku.check1()

#### PRINT SUDOKU

#for a in row:
#  print(a)
