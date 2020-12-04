dst = gets.chomp.to_f
rrs = gets.chomp.to_f
cys = gets.chomp.to_f
rrtts = dst / rrs
cytts = (dst + 50) / cys
if rrtts < cytts
  puts 'Meep Meep'
else
  puts 'Yum'
end

