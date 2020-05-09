import os
os.system("clear")

import math

colors = int(input())
can_br = 40
p_paint = 5
tax = (colors * p_paint + can_br) * 10 / 100

money = math.ceil(can_br + colors * p_paint + tax)
print(money)