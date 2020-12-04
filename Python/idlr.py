word = input() or 'AaabBbbc'
word = list(word[x] for x in range(len(word)))
word = list(dict.fromkeys(word).keys())
word = ''.join(word)
print(word)
