#!/data/data/com.termux/files/usr/bin/fish

  clear
  set text (string split '' ' Probando nuevo prompt... ')

  set n 689; set n1 $n
  set s (math -s0 (string length "$text")/20)
  if [ (string length "$text") -le 21 ]; set s 1; end

  for z in (seq 1 $s (count $text))
      set t $text[$z..(math $z + $s - 1)]
      for x in (seq (count $t))
  	set y "$y"(set_color -b $n1)$t[$x](set_color -b normal)
      end

      if ! [ $n1 -eq (math $n - 9) ]
        set n1 (math $n1 - 1)
      end
      set prompt $y
  end

  echo $prompt
#--------------------------------
for c in (seq 0 999)
  if test $c -lt 10; set c "00"$c;end
  if test $c -ge 10 -a $c -lt 100; set c "0"$c;end
    echo (set_color -b $c)" $c "(set_color normal)
end