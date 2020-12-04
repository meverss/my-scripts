age = gets.chomp.to_i
time = gets.chomp.to_i

a = age + time
td = a - age

puts 'My twin is #{a} years old and they are #{td} years older than me'