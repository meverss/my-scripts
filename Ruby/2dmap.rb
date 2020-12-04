map2d = gets.chomp.split(',')
cidx = []
ridx = []
mode = 0

for a in (0...5)
  if map2d[a].include? "P"
    if map2d[a].count('P') == 1
      cidx << map2d[a].index('P')
      ridx << a
      mode = 0
    elsif map2d[a].count('P') == 2
      cidx << map2d[a].index('P')
      cidx << map2d[a].rindex('P')
      mode = 1
    end
  end
end

if mode == 0
  cidx = cidx.sort()
  ridx = ridx.sort()
  p1 = cidx[1] - cidx[0]
  p2 = ridx[1] - ridx[0]
  steps = p2 + p1
elsif mode == 1
  steps = cidx[1] - cidx[0]
end

print(steps)