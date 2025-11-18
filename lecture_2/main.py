# Function that determines the user's life stage (Child / Teenager / Adult)
def generate_profile(age):
    if age < 0:
        raise ValueError('The age cannot be bellow zero')
    elif age < 13:
        return 'Child'
    elif age < 20:
        return 'Teenager'
    else:
        return 'Adult'


# Constant that represents the current year (used to calculate age)
current_year = 2025

# Empty list to store user hobbies
hobbies = []


# --- User input: name ---
user_name = input('Enter your full name: ')
if user_name == '':
    raise ValueError('name cannot be empty')


# --- User input: birth year ---
birth_year_str = input('Enter your birth year: ')
try:
    # Convert string to integer
    birth_year = int(birth_year_str)

    # Check if birth year is within valid range
    if not (0 < birth_year <= current_year):
        raise ValueError("incorrect birth year")
except:
    # Triggered if conversion to int fails
    raise ValueError('incorrect birth year')


# Calculate user's current age
current_age = current_year - birth_year


# --- Loop to collect hobbies ---
while True:
    hobby = input("Enter a favorite hobby or type 'stop' to finish: ")

    # Allow stopping the hobby input process
    if hobby.strip().lower() == 'stop':
        break

    # Add hobby to the list
    hobbies.append(hobby)


# Determine user's life stage based on age
life_stage = generate_profile(current_age)


# Store all profile information in a dictionary
user_profile = {
    'Name' : user_name,
    'Age': current_age,
    'Life Stage': life_stage,
    'Favorite Hobbies': hobbies
    }


# --- Output Section ---
print('---')
print('Profile Summary:')

# Display each field of the profile
for key, val in user_profile.items():

    # Print name, age and life stage normally
    if key != "Favorite Hobbies":
        print(f"{key}: {val}")

    # Special logic for the hobbies list
    else:

        # Checking whether the hobbies list is empty
        if not val:
            print("You didn't mention any hobbies")
        else:
            print(f'{key} ({len(val)}):')
            for hobby in val:
                print(f'- {hobby}')

print('---')