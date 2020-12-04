string = input()

for a in string:
  if a == a.upper():
    string = string.replace(a,f"_{a.lower()}")
string = list(string)
if string[0] == '_':
  string.pop(0)
string = ''.join(string)
print(string)