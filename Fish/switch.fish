#!/data/data/com.termux/files/usr/bin/fish

clear
read -p 'echo "Number: "' -n 2 -l f
set a (seq 12)
if contains $f (seq 12)
  echo "Opcion $f"
end