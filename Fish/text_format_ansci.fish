#!/data/data/com.termux/files/usr/bin/fish

clear
set format Bold Underline Reverse Reset Teal Green Gold
set Bold "\u001b[1m"
set Underline "\u001b[4m"
set Reverse "\u001b[7m"
set Reset "\u001b[0m"
set Teal "\u001b[38;5;31m"
set Green "\u001b[38;5;70m"
set Gold "\u001b[38;5;220m"

for x in (seq (count $format))
  printf "$$format[$x]"$format[$x]"\u001b[0m"\n\n
end
