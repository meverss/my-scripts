colors = gets.chomp.to_i
cb = 40.00
c_price = 5
sell = colors * c_price + cb
tax = sell * 10 / 100
bill = sell + tax
puts bill.ceil()
