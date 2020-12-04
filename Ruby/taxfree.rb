prices = gets.chomp.split(",")
total = 0
for a in (0...prices.length)
  prices[a] = prices[a].to_f
end
for b in prices
  if b <= 20
    b += b * 7 / 100
    total += b
  else
    total += b
  end
end

puts '%.2f' % total