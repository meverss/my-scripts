i = 1
rgb_colors = []
hex_colors = []
r = int(input())
g = int(input())
b = int(input())

def conv_color(red, green, blue):
  red = hex(red)[2:]
  green = hex(green)[2:]
  blue = hex(blue)[2:]
  hex_colors = (f"#{red}{green}{blue}")
  return hex_colors

print(conv_color(r,g,b))