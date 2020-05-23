from math import ceil
h = int(input())
w = int(input())

duct = ceil((h*12*w*12)/(60*12*2))*2
print(duct)