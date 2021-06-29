#!/data/data/com.termux/files/usr/bin/fish

clear
set hex a b c d e f

for b in (seq (count $b_lang))
    if [ $b -le 9 ]
	set c_hex $hex[1]
    else if [ $b -ge 10 -a $b -le 19 ]
        set c_hex $hex[2]
    else if [ $b -ge 20 -a $b -le 29 ]
        set c_hex $hex[3]
    else if [ $b -ge 30 -a $b -le 39 ]
        set c_hex $hex[4]
    else if [ $b -ge 40 -a $b -le 49 ]
	set c_hex $hex[5]
    else if [ $b -ge 50 -a $b -le 59 ]
	set c_hex $hex[6]
    end

    set f (math $f + 1)
    if [ $f -eq 10 ]
        set f 1
    end

    if [ $b -le 9 ]
	set cnt "0$b-$b_lang[$b] "
    else
	set cnt "$b-$b_lang[$b] "
    end

    echo (set_color 75$f$c_hex(math $b + 29))$cnt(set_color normal)
#    echo 75$f$c_hex(math $b + 29)
end
