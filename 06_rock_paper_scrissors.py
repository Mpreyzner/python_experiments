import random
options = ['rock', 'paper', 'scissors']

beats = {'rock': 'scissors', 'paper': 'rock', 'scissors': 'paper'}

while True:
    user_choice = input("Pick rock, paper or scissors: \n")
    machine_choice = random.choice(options)
    print("So it's " + str(user_choice) + ' versus ' + machine_choice)
    if beats[user_choice] == machine_choice:
        print('You won')
    elif beats[machine_choice] == user_choice:
        print('Machine won')
    else:
        print("It's a draw \n")
