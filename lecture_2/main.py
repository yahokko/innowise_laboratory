user_name =input('Enter your full name: ')
user_birth_year = int(input('Enter your birth year: '))

user_age = 2025 - user_birth_year

user_hobbies = []

while True:
    hobby = input("Enter a favorite hobby or type 'stop' to finish: ")
    if hobby.lower() == 'stop':
        break
    user_hobbies.append(hobby)

def age_check(age):
    if age < 0:
        raise ValueError('The age cannot be bellow zero')
    elif age < 13:
        return 'Child'
    elif age < 20:
        return 'Teenager'
    else:
        return 'Adult'
    
user_life_stage = age_check(user_age)

print('-'*3)
print('Profile Summary:')
print(f'Name: {user_name}')
print(f'Age: {user_age}')
print(f'Life Stage: {user_life_stage}')
if not user_hobbies:
    print("You didn't mention any hobbies")
else:
    print(f'Favorite Hobbies ({len(user_hobbies)}):')
    for hobby in user_hobbies:
        print(f'- {hobby}')
print('-'*3)
