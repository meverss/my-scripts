snack = gets.chomp.split(" ")
snak = snack.map(&:capitalize!)
izzy = 0

menu = {
     "Lettuce" => 5,
     "Carrot" => 4,
     "Mango" => 9,
     "Cheeseburger" => 0
     }

for a in snack
  if menu[a]
    izzy += menu[a]
  end
end

if izzy >= 10
  print('Come on Down!')
else
  print('Time to wait')
end
