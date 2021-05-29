#!/data/data/com.termux/files/usr/bin/fish

clear
set text (string split '' ' Probando nuevo prompt... ')

for c1 in (seq 3)
set n $c1"09"; set n1 $n
#set n 109; set n1 $n
set s (math -s0 (string length "$text")/20)
if [ (string length "$text") -le 21 ]; set s 1; end

for z in (seq 1 $s (count $text))
echo $z - $s
    set t $text[$z..(math $z + $s - 1)]
    for x in (seq (count $t))
	set y "$y"(set_color -b $n1)$t[$x](set_color -b normal)
    end

    if ! [ $n1 -eq (math $n - 9) ]
        set n1 (math $n1 - 1)
    end
    set txt "* $y"

end
#end
echo $txt
end

#end


#for c in (seq 100 999)
#    echo (set_color -b $c)" $c "(set_color normal) | more
#end