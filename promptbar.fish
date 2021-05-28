#!/data/data/com.termux/files/usr/bin/fish

clear
set text (string split '' ' Esto es una prueba de lo que hacemos... ')

set n 999; set n1 $n
for z in (seq (count $text))
    set txt "$txt"(string join0 (set_color -b $n1)$text[$z](set_color normal))
#    if ! [ $n1 -eq (math $n - 9) ]
    set n1 (math $n1 - 111)
    if [ $n1 -le 111 ]
        set n1 111
#        set n1 (math $n1 - 111)
    end
end

echo $txt

#for c in (seq 100 999)
#    echo (set_color -b $c)" $c "(set_color normal) | more
#end