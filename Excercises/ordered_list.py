import os
os.system("clear")

qt = int(input("How many words do you need? "))
word = ''
lista = []

a = 1
while a <= qt:
  word = input("Word" + (str(a)) + ": ")
  lista.append(word)
  a += 1

lista.sort()

print(lista)