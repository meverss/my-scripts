import os
os.system("clear")

casino = input()
status = ''

p_guard = 0
p_money = 0
p_thief = 0
if "G" in casino:
  p_guard = casino.rindex("G")
  p_guard = int(p_guard)
else:
  status = "alarm"
if "T" not in casino:
  status = "quiet"
if "$" in casino:
  p_money = casino.index("$")
else:
  status == "quiet"
if "T" in casino:
  p_thief = casino.index("T")

if p_guard >= p_thief and p_money >= p_guard or p_guard >= p_money and p_thief >= p_guard:
 status = "quiet"
else:
 status = "alarm"

if status == "alarm":
  print("ALARM")
elif status == "quiet":
  print("quiet")