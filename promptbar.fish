#!/data/data/com.termux/files/usr/bin/fish

#clear
set text (string split '' ' Esto es una prueba de lo que hacemos... ')

set n 189; set n1 $n
set s (math -s0 (string length "$text")/20)
if [ (string length "$text") -le 21 ]; set s 1; end
for z in (seq 1 $s (count $text))
    set t $text[$z..(math $z + $s - 1)]
    for x in (seq (count $t))
	set y "$y"(string join0 (set_color -b $n1)$t[$x](set_color normal))
    end
    set txt (string join0 $y)
    if ! [ $n1 -eq (math $n - 9) ]
        set n1 (math $n1 - 1)
    end
end
echo $txt

#for c in (seq 100 999)
#    echo (set_color -b $c)" $c "(set_color normal) | more
#end