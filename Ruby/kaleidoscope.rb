k = gets.chomp.to_f

if k > 1 && k != 3
  sale = (k*5)-(0.5*k)
  tax = 7*sale/100                                             
  sale += tax
  puts sale.to_s[0..4]
elsif k == 3
  sale = (k*5)-(0.5*k)
  tax = 7*sale/100
  sale += tax
  puts '%.2f' % sale.round(2)
else
  sale = k*5
  tax = 7*sale/100
  sale += tax
  puts '%.2f' % sale#.round(2)
end
