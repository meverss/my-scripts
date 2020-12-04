cmyk = []

for x in range(4):
  color = input()
  cmyk.append(color)

for a in range(len(cmyk)):
  cmyk[a] = float(cmyk[a])
R = round(255 * (1 - cmyk[0]) * (1 - cmyk[3]))
G = round(255 * (1 - cmyk[1]) * (1 - cmyk[3]))
B = round(255 * (1 - cmyk[2]) * (1 - cmyk[3]))

print(f"{R},{G},{B}")