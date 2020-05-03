#!/data/data/com.termux/files/usr/bin/fish

## Lista desordenada
set a (list)
for x in (seq (count $a))
    set -a lista $a[$x]
end
clear && shuf -e $lista
