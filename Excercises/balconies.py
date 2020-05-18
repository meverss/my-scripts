ap_a = input().split(",")
ap_b = input().split(",")

area_a = int(ap_a[0]) * int(ap_a[1])
area_b = int(ap_b[0]) * int(ap_b[1])

if area_a > area_b:
  print('Apartment A')
else:
  print('Apartment B')
