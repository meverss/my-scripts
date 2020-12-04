"""
Author: MeVeRsS

Description:

This code shows how to use the library <colored> to color
and formatting in terminal.

It prints a list of all available colors (256) and their
corresponding code (color 0 is black).

Colors can be also refered by their description ("yellow",
"orange_red_1") or HEX code (#cb4b16).

Refer to atributes by their description or code.

Use <pip> to install the library:

pip install colored

Main use::

fg()	Foreground color
bg()	Background color
attr()	Attributes
"""

from colored import fg, bg, attr
import os

clear = os.system("clear")
clear

title = (f"{fg('#cb4b16')}{bg(235)}")
question = (f"{fg(245)}{attr('bold')}")
header = (f"{fg(185)}{attr(1)}")
normal = attr("reset")

print(f"{title} COLORS {normal}")
i=0
while i <= 255:
  print(f"{fg(i)}{str(i)}	{fg(i+1)}{str(i+1)}	{fg(i+2)}{str(i+2)}	{fg(i+3)}{str(i+3)}	{fg(i+4)}{str(i+4)}	{fg(i+5)}{str(i+5)}	{fg(i+6)}{str(i+6)}	{fg(i+7)}{str(i+7)}")
  i += 8

print()
print(f"{title} ATTRIBUTES {normal}")
print("+-----+-----------------+")
print(f"|{header}Code{normal} |{header} Description{normal} 	|")
print("+-----+-----------------+")
print("|  1  | bold 		|")
print("|  2  | dim 		|")
print("|  4  | underlined 	|")
print("|  5  | blink 		|")
print("|  7  | reverse 	|")
print("|  8  | hidden 		|")
print("|  0  | reset 		|")
print("| 21  | res_bold 	|")
print("| 22  | res_dim 	|")
print("| 24  | res_underlined 	|")
print("| 25  | res_blink 	|")
print("| 27  | res_reverse 	|")
print("| 28  | res_hidden 	|")
print("+-----------------------+")

text = (input(f"{question}Enter colors for sample (fg, bg, attr): {normal}")).split(",")
if text != "":
  if text[0] == '':
    text[0] = 0
  elif text[1] == '':
    text[1] = 0
  elif text[2] == '':
    text[2] = 5
    print(f"{fg(int(text[0]))}{bg(int(text[1]))}{attr(int(text[2]))} This is a sample text ")
