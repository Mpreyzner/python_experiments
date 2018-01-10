
def get_score(first_name, second_name):
    crammed = first_name + second_name
    letters = list(crammed)
    unique_letters = list(set(letters))
    score = 0
    for letter in unique_letters:
        score = score + ord(letter)
    remainder = score % 101
    return remainder


first_name = input('Enter your name')
second_name = input('Enter partner name')

print('Your love score is ' + str(get_score(first_name, second_name)) + '%')
