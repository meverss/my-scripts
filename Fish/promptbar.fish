#!/data/data/com.termux/files/usr/bin/fish

  clear
  barracuda_reload
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
function rgb
for c2 in a b c d e f
  for c1 in a b c d e f  
    for c3 in (seq 0 9)
    set s (set_color normal)(set_color -b green)"  "(set_color normal)
      echo (set_color -b $c1$c2$c3 red)" $c1$c2$c3 "(set_color normal)$s\
           (set_color -b $c1$c3$c2 red)" $c1$c3$c2 "(set_color normal)$s\
           (set_color -b $c2$c1$c3 red)" $c2$c1$c3 "(set_color normal)$s\
           (set_color -b $c2$c3$c1 red)" $c2$c3$c1 "(set_color normal)$s\
           (set_color -b $c3$c1$c2 red)" $c3$c1$c2 "(set_color normal)$s\
           (set_color -b $c3$c2$c1 red)" $c3$c2$c1 "(set_color normal)$s
    end
  end
end       
end

function hex 
for x in (seq 1 999)
  if test $x -lt 10; set x "00"$x;end
  if test $x -ge 10 -a $x -lt 100; set x "0"$x;end
  echo (set_color -b $x)"  $x  "(set_color normal)(set_color -b green)"     "(set_color normal)
end
end

hex