#!/data/data/com.termux/files/usr/bin/fish

clear
read -p 'echo Escribe: ' -l argv
if test $argv = 'marv'
  echo Hacker
else
  echo Naah..
end
echo "Escribiste $argv" 