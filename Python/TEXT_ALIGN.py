from shutil import get_terminal_size as ts

class align():
  def __init__(align):
    self.align = align

  def centered(string):
    width = int(ts()[0])
    return (string.center(width))

  def right(string):
    width = int(ts()[0])
    return (string.rjust(width))

  def left(string):
    width = int(ts()[0])
    return (string.ljust(width))

text = 'Marvin Eversley Silva'
text1 = ' Esto es una peueba '

print(align.centered(text))
print(align.right('ERES UN SALVAJE\n'))
print(text1.center(ts()[0],"="))  # .center(width,refill_char)