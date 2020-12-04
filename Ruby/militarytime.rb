time = gets.chomp.upcase.split(':')
if time[1].include? 'PM' and time[0].to_i <= 11
  H = time[0].to_i + 12
  HH = "#{H}:#{time[1][0..1]}"
  print HH
elsif time[0].to_i == 12  and time[1].include? 'AM'
  H = '00'
  HH = "#{H}:#{time[1][0..1]}"
  print(HH)
elsif time[0].to_i <= 12  and time[1].include? 'AM'
  if time[0].to_i <= 9
    H = "0#{time[0]}"
  else
    H = time[0]
  end
  HH = "#{H}:#{time[1][0..1]}"
  print(HH)
elsif time[0].to_i == 12  and time[1].include? 'PM'
  H = time[0]
  HH = "#{H}:#{time[1][0..1]}"
  print(HH)
end
