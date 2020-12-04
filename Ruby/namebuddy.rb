group = gets.chomp.upcase().split(" ")
v = 0
myname = gets.chomp.upcase()

for a in group
  if myname[0] == a[0]
    v = 1
    break
  else
    v = 0
  end
end

if v == 1
  print('Compare notes')
elsif v == 0
  print('No such luck')
end
