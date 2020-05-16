from shutil import get_terminal_size as ts

class text_align():
  def __init__(align):
    self.align = align

  def centered(string):
    width = int(ts()[0])
    return (f"{string:^{width}}")

  def right(string):
    width = int(ts()[0])
    return (f"{string:{width}}")

text = 'Marvin Eversley Silva'
text1 = ' Esto es una peueba '

print(text_align.centered(text))
print(text_align.centered('ERES UN SALVAJE\n'))
print(text1.center(ts()[0],"="))  # .center(width,refill_char)