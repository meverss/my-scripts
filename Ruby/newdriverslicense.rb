name = gets.chomp
agents = gets.chomp.to_f
others = gets.chomp
cue = "#{name} #{others}".split(' ')
cue.map(&:capitalize!)
cue = cue.sort()

my_turn = cue.index(name.capitalize) + 1
puts my_turn

if my_turn >= agents
  rnd = (my_turn / agents).ceil()
  license = rnd * 20
else
  license = 20
end

print(license)
