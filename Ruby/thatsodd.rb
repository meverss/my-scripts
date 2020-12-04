n = gets.chomp.to_i
i = 1
x = 0
while i <= n
  num = gets.chomp.to_i
  if num % 2 == 0
    x += num
  end
  i += 1
end
puts x
