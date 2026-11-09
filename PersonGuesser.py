import math

valid_input = 0

print('''Welcome to the program!
         Input years by typing any number, positive or negative.
         Negative numbers translate to BCE years, while positive numbers translate to CE years.
         For example, if you wanted to have 2026, you would simply just type 2026.
         For something like 300 BCE, you would type -300.
         That's it!''')

while valid_input == 0:
    user_birth_year = input('Please input your birth year:\n')
    mother_birth_year = input('Now input the birth year of your Mother:\n')
    secret_person_birth_year = input('''Now enter the birth year of the person that you want the program to guess who it is.
                The program assumes this is your relative.
''')
    try:
        user_birth_year = float(user_birth_year)
        if not math.isfinite(user_birth_year):
            print('Please enter valid numbers.')
            continue
        mother_birth_year = float(mother_birth_year)
        if not math.isfinite(mother_birth_year):
            print('Please enter valid numbers.')
            continue
        secret_person_birth_year = float(secret_person_birth_year)
        if not math.isfinite(secret_person_birth_year):
            print('Please enter valid numbers.')
            continue

        if user_birth_year == 0 or mother_birth_year == 0 or secret_person_birth_year == 0:
            print('Birth year must not be 0.')
            continue

        if mother_birth_year >= user_birth_year:
            print(
                'It is physically impossible that you are older than your mother or have the exact same age.\nPlease enter valid numbers.')
            continue
        valid_input = 1
    except ValueError:
        print('Please enter valid numbers.')

if (secret_person_birth_year > 0 and user_birth_year < 0) or (secret_person_birth_year < 0 and user_birth_year > 0):
    distance = abs(secret_person_birth_year - user_birth_year) - 1
else:
    distance = abs(secret_person_birth_year - user_birth_year)

def return_message():
    generation = False
    if secret_person_birth_year == mother_birth_year:
        return '''Thought the program wouldn't know it? As easy as pie! This person is definitely your mother!
If not, this person is most likely your dad OR a sibling/cousin of your parent!'''
    if secret_person_birth_year >= user_birth_year:
        if secret_person_birth_year == user_birth_year:
            return '''What a fool, trying to see if the program can guess them!
Just kidding, anyways, this person is most likely you yourself OR your sibling OR your cousin!'''
        if distance <= 15:
            return '''This person is most likely your sibling OR your cousin.'''
        if distance <= 50:
            return '''This person is most likely your child OR a sibling/cousin of your child.'''
        generation_found = False
        number = 0
        while generation_found == False:
            number += 1
            if secret_person_birth_year <= (user_birth_year + 50 + number*25):
                generation_found = True
                generation = number-1
        name = generation*'great-'+'grandchild'
        if generation == 0:
            return '''This person is most likely your grandchild OR a sibling/cousin of your grandchild.'''
        elif generation == 1:
            return '''This person is most likely your great-grandchild OR a sibling/cousin of your great-grandchild.'''
        else:
            return f'''This person is most likely your {generation}x-great-grandchild OR
a sibling/cousin of your {generation}x-great-grandchild({name})'''

    else:
        if distance <= 15:
            return '''This person is most likely your sibling OR your cousin.'''
        if distance <= 50:
            return '''This person is most likely your parent OR a sibling/cousin of your parent.'''
        generation_found = False
        number = 0
        while generation_found == False:
            number += 1
            if secret_person_birth_year >= (user_birth_year - 50 - number*25):
                generation_found = True
                generation = number-1
        name = generation*'great-'+'grandparent'

        if generation == 0:
            return '''This person is most likely your grandparent OR a sibling/cousin of your grandparent.'''
        elif generation == 1:
            return '''This person is most likely your great-grandparent OR a sibling/cousin of your great-grandparent.'''
        else:
            return f'''This person is most likely your {generation}x-great-grandparent OR
a sibling/cousin of your {generation}x-great-grandparent({name})'''

print(return_message())