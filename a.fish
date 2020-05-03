#!/data/data/com.termux/files/usr/bin/fish

set shop "milk" "cookies" "bread"
set milk condensed natural
set cookies coconuts vanilla strawberry chocolatte
set bread llanero soft cheese-bread

for a in (seq (count $shop))
  echo $a- $shop[$a]
  for b in (seq (count $$shop[$a]))
    echo '    '- $$shop[$a][$b]
  end
  echo
end