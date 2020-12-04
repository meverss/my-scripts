"""
Title:		message-encrypt
Author:		MeVeRsS <meverss@outlook.com>
Last Update:	Wed May 6 23:56:59 CDT 2020

Description:	This is a simple code to encrypt texts.
"""
import os,colors
os.system("clear")

from string import punctuation as symbols, digits
from random import randint as rnd

def encrypted(msg):
  msg = list(msg [::-1])
  tmp = msg.copy()
  i = 0
  while i <= len(msg) * 2:
    tmp.insert(rnd(0,len(tmp)-1),symbols[rnd(0,len(symbols)-1)])
    tmp.insert(rnd(0,len(tmp)-1),digits[rnd(0,len(digits)-3)])
    i += 1
  tmp = ''.join(tmp)
  msg = tmp
  return msg

text = input('Enter text: ')
print(colors.color(encrypted(text),bg='blue',fg='black',style='faint'))
print("Hola!")
