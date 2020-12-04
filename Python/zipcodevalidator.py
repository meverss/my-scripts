from string import digits, ascii_letters as letters
zcode = input()

if len(zcode) == 5 and zcode.isdigit():
  print("true")
else:
  print("false")