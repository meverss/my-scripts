from shutil import get_terminal_size as ts

class text_align():
  def __init__(align):
    self.align = align

  def centered(string):
    width = ts()
    width = int(width[0])
    return (f"{string:^{width}}")

text = 'Marvin Eversley Silva'

print(text_align.centered(text))
print(text_align.centered('ERES UN SALVAJE'))