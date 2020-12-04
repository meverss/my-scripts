n = gets.chomp.to_i
l = gets.chomp.split()
l = l.map(&:to_i)
t = l.all? { |x| n%x == 0 }
if t == true
  puts'divisible by all'
else
  puts 'not divisible by all'
end