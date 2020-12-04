prices = gets.chomp.split(',')
prices = prices.map(&:to_f).sort().reverse()
disc =  prices[1..].map { |x| x - (30 * x / 100) }
disc = disc.sum()
tntax = prices[0] + disc
sntax = prices.sum() - tntax
tax = 7 * sntax / 100
save = sntax + tax
puts save.to_i