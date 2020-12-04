str = gets.chomp.downcase.split()
str = str.map { |x| x << x[0] &&  x << 'ay' && x=x[1..]}
print str.join(' ')
