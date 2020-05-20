n_names = int(input())
initials = []
for a in range(n_names):
  name = (input().title()).split(" ")
  initials.append(f"{name[0][0]}{name[1][0]}")

initials = ' '.join(initials)

print(initials)