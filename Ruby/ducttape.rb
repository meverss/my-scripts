h = gets.chomp.to_f
#h *= 12
w = gets.chomp.to_f
#w *= 12
=begin
area = h * w
a_tape = 2 * (60 * 12)
need = area / a_tape# * 2
=end
duct = ((h*12*w*12)/(60*12*2)).ceil() * 2
puts duct
