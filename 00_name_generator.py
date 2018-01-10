import random;

gender = ['male', 'female']
male_names = ['Jack', 'Pate', 'Jerry']
female_names = ['Anna', 'Hanna']
names = {'male': male_names, 'female': female_names}

choosen_gender = input("Please select a sex male/female: ")
if choosen_gender not in gender:
    raise Exception('Enter proper gender')

name_key = random.randint(0, len(names[choosen_gender]) - 1)

random_name = names[choosen_gender][name_key]


surnames = ['Walsh', 'Beck', 'Martin', 'Poe']
surname_key = random.randint(0, len(surnames) -1 );

random_surname = surnames[surname_key]

prefixes = {'male': ['Mr'], 'female': ['Miss', 'Mrs']}
random_prefix = random.choice(prefixes[choosen_gender])

print(random_prefix + ' ' + random_name + ' ' + random_surname)
