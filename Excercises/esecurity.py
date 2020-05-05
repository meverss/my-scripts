string = input()

if s in string == "G":
  p_guard = string.index("G")
else:
  situation = alarm
p_money = string.index("$")
p_thief = string.index("T")

if p_guard >= p_money and p_guard <= p_tbief:
  situation = quiet
else:
  situation = alarm

if situation == alarm:
  print("ALARM")
else:
  print("quiet")