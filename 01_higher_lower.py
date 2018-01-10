import random;

result = random.randint(0,42)
guessed = False
while not guessed:
    guess = int(input('Guess number between 0 and 42 '))

    if guess == result:
        print('You won!! The number was:' + str(guess))
        guessed = True
    if guess < result:
        print('Higher')
    elif guess > result:
        print('Lower')
