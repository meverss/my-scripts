str = gets.chomp.split('')
v = 'aeiouAEIOU'.split('')
vowels = str.select {|x| v.include? x}
puts vowels.length