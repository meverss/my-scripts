points = gets.chomp.to_i
price = gets.chomp.to_i
tickets = points / 12
if tickets >= price
  puts 'Buy it!'
else
  puts 'Try again'
end

