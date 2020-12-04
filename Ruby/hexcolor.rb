hex = []
for i in (1..3)
  n = gets.chomp.to_i
  hex << n
end
puts "#%02x%02x%02x" % hex
