blocks = gets.chomp.upcase or "BBHBBP"
#blocks = list(blocks)

h = blocks.index("H")
p = blocks.index("P")
#puts h
#=begin
if h > p
  distance = h-p-1
elsif p > h
  distance = p-h-1
end
#=end

print(distance)