list = gets.chomp.split(' ')
list = list.map(&:to_i)
list = list.select { |x| x.odd? }
print list

