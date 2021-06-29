#!/data/data/com.termux/files/usr/bin/fish

set shop 'Milk' Butter "Cookies" "Bread"
set Milk Condensed Natural
set Cookies Coconuts Vanilla Strawberry Chocolatte
set Bread Llanero Soft "Cheese bread"

for a in (seq (count $shop))
  echo $a-$shop[$a]
  for b in (seq (count $$shop[$a]))
    echo '    '- $$shop[$a][$b]
  end
  echo
end
echo $$shop[3]