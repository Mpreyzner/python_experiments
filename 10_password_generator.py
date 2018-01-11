import random
from random_words import RandomWords


length = input('How long you want your password (in number of words?')

if not length.isdigit():
    raise Exception('Enter a number silly')

rw = RandomWords()
words = rw.random_words(count=int(length))
password = ' '.join(words)
print(password)
