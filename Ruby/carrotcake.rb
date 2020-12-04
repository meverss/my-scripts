carrots = gets.chomp.to_i
boxes = gets.chomp.to_i

cfc = carrots % boxes

if cfc >= 7
  puts "Cake Time"
else
  puts "I need to buy #{7 - cfc} more"
end

