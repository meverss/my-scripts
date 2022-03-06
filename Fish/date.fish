#!/bin/fish

clear
set orig "Apr 28 07:50:01" 
set epoch (date -d "$orig" +"%s")
set epoch_to_date (date -d @$epoch +"%Y%m%d_%H%M%S")
set ext_date (date -d @$epoch +"%A, %B %d %Y - %I:%M:%S %p")
echo "RESULTS:"
echo "Original = $orig"
echo "Epoch convertion = $epoch" 
echo "Epoch to human readable time stamp = $epoch_to_date"
echo "Extended time stamp = $ext_date"