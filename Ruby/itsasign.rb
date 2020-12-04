a = 1
words = []
openb = ''
while a <= 4
  word = gets.chomp.upcase
  words << word
  a += 1
end

for i in words
  if i == i.reverse
    openb = 'yes'
    break
  end
end

if openb == 'yes'
  print('Open')
else
  print('Trash')
end
