msg = input()
msg = msg.lower()
msg = msg.split(" ")
abc = "abcdefghijklmnopqrstuvwxyz"
e_abc = list(abc [::-1])
n_msg = ""
i = 0
while i <= (len(msg) - 1):
  n_word = ""

  for a in msg[i]:
    ch = list(abc).index(a)
    e_ch = e_abc[ch]
    n_word += e_ch

  n_msg = list(n_msg)
  n_msg.append(n_word)
  i += 1
n_msg = ' '.join(n_msg)
print(n_msg)