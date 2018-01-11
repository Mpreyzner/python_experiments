import random

question = input('Please enter your guestion')
answers = {
    'yes':       ['It is certain',
                  'It is decidedly so',
                  'Without a doubt',
                  ' Yes definitely',
                  'You may rely on it',

                  'As I see it, yes',
                  ' Most likely',
                  ' Outlook good',
                  'Yes',
                  'Signs point to yes', ],
    'uncertain': [
        ' Reply hazy try again',
        ' Ask again later',
        ' Better not tell you now',
        'Cannot predict now',
        ' Concentrate and ask again', ],
    'no':        [
        " Don't count on it",
        ' My reply is no',
        ' My sources say no',
        'Outlook not so good',
        ' Very doubtful ', ]
}
print(answers.keys())
finished = False
answer = random.choice(list(answers.keys()))
answer_content = random.choice(answers[answer])

print('So the answer to: ' + question + "is \n" + answer_content)
# add reasking when uncertain
