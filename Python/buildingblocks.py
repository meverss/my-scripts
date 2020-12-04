blue = int(input())
red = int(input())
green = int(input())
yellow = int(input())

bleft = (blue % 15) + (red % 15) + (green % 15) + (yellow % 15)

print(f"{bleft}")