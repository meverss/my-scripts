string = gets.chomp.split('')
isogram = string.all? { |x| string.count(x) == 1 }
puts isogram