string = list(input())
parts = int(input())

a=0
while a <= len(string)-1:
    string.insert(a+parts,"-")
    a += parts+1

string.pop(-1)
string = ''.join(string)
print(string)