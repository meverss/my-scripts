ahead = gets.chomp.to_f
trip = ((ahead + 1) / 20).ceil()
time = 0
if trip == 1
 time = 10
else
 time = trip * 20 - 10
end

print(time)