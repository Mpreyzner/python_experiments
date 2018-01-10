from random_words import RandomWords

rw = RandomWords()
word = rw.random_word()
guessed = False
print(word)

result = list(len(word) * '*')


def substitute(letter, word, result):
    for i in range(len(word)):
        if word[i] == letter:
            result[i] = letter;
    return result


def is_guessed(word, result):
    if ''.join(result) == word:
        return True
    else:
        return False


while not guessed:
    letter = input('Pick a letter')

    if len(letter) > 1:
        raise Exception('Pick ONE letter silly')
# add check against not letters :D

    if letter in word:
        print("Woohoo\n")
        result = substitute(letter, word, result)
        print(result)
    else:
        print("Ooops!\n")

    guessed = is_guessed(word, result)
