string = input()
isogram = all(string.count(x) == 1 for x in string)
print(str(isogram).lower())

