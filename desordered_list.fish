#!/data/data/com.termux/files/usr/bin/fish

## Lista desordenada

set a (list)
for x in (seq (count $a))
    echo $x >> tmp_list
end
set -a lista (cat tmp_list | sort -R && rm tmp_list)
for i in (seq (count $a))
    echo $a[$lista[$i]]
end
