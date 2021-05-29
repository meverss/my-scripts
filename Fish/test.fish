#!/data/data/com.termux/files/usr/bin/fish

clear
set format bold_ansi_code underline_ansi_code reversed_ansi_code reset_ansi_code teal_ansi_code green_ansi_code gold_ansi_code
set -l bold_ansi_code "\u001b[1m"
set -l underline_ansi_code "\u001b[4m"
set -l reversed_ansi_code "\u001b[7m"
set -l reset_ansi_code "\u001b[0m"
set -l teal_ansi_code "\u001b[38;5;31m"
set -l green_ansi_code "\u001b[38;5;70m"
set -l gold_ansi_code "\u001b[38;5;220m"

for x in (seq (count $$format))
  printf "$$format[$x] Marvin"\n
end
