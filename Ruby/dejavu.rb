str = gets.chomp
stat = ''
i=0
while i <= (str.length - 2)
  if str[i] == str[i + 1]
      stat = 'dejavu'
      break
  else
      stat = 'unique'
  end
  i += 1
end
if stat == 'unique'
  puts 'Unique'
elsif stat == 'dejavu'
  puts 'Deja Vu'
end