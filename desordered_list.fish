#!/data/data/com.termux/files/usr/bin/fish

## Lista desordenada
set a (ls)
for x in (seq (count $a))
    set -a lista $a[$x]
end
shuf -e $lista
