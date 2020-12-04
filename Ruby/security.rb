casino = gets.chomp
status = ''

p_guard = 0
p_money = 0
p_thief = 0
if casino.include? "G"
  p_guard = casino.rindex("G")
  puts p_guard
else
  status = "alarm"
end
if not casino.include? "T"
  status = "quiet"
end
if casino.include? "$"
  p_money = casino.index("$")
else
  status == "quiet"
end
if casino.include? "T"
  p_thief = casino.index("T")
end

if p_guard >= p_thief and p_money >= p_guard or (p_guard >= p_money and p_thief >= p_guard)
 status = "quiet"
else
 status = "alarm"
end

if status == "alarm"
  print("ALARM")
elsif status == "quiet"
  print("quiet")
end
