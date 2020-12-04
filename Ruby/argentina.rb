p_pesos = gets.chomp.to_i
p_dollars = gets.chomp.to_i
if (p_pesos * 0.02) < p_dollars
  puts 'Pesos'
else
  puts 'Dollars'
end
puts 80 == 80.0