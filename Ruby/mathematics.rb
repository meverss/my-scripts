result = gets.chomp.to_i
expr = gets.chomp.split(" ")
check = ''
#=begin
for a in expr
  if eval(a) == result
    check = 'ok'
    break
  end
end

if check == 'ok'
  puts "index #{expr.index(a)}"
else
  print('none')
end
