import random;

gender = ['male', 'female']
male_names = ['Jack', 'Pate', 'Jerry']
female_names = ['Anna', 'Hanna']
names = {'male': male_names, 'female': female_names}


gender = gender[random.randint(0, 1)]

name_key = random.randint(0, len(names[gender]) - 1)

random_name = names[gender][name_key]


surnames = ['Walsh', 'Beck', 'Martin', 'Poe']
surname_key = random.randint(0, len(surnames) -1 );


random_surname = surnames[surname_key]

print(random_name + ' ' + random_surname)
