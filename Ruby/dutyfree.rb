items = gets.chomp.split(' ')
items = items.map(&:to_f)
check = items.any? { |x| x * 1.1 > 20 }
if check == true
  puts 'Back to the store'
else
  puts 'On to the terminal'
end