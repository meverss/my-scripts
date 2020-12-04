ap_a = gets.chomp.split(',')
ap_b = gets.chomp.split(',')
ap_a = ap_a.map(&:to_i)
ap_b = ap_b.map(&:to_i)
areaA = ap_a[0] * ap_a[1]
areaB = ap_b[0] * ap_b[1]
if areaA > areaB
  puts 'Apartment A'
elsif areaB > areaA
  puts 'Apartment B'
end