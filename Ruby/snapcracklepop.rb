i = 1
sounds = []
while i <= 6
  rk = gets.chomp.to_i
    if rk % 3 == 0
      sounds << 'Pop'
    elsif rk % 3 != 0 and rk % 2 != 0
      sounds << 'Snap'
    elsif rk % 3 != 0 and rk % 2 == 0
      sounds << 'Crackle'
    end
  i += 1
end
print sounds.join(' ')
