# Tristan Kendall
# Date: 2025-06-25
# CMP131 - Foundations of Programming (Python)
# Project: Mid-Term 1 - Cruise Activities
# Academic Integrity Acknowledgment: yes

# Boolean flag
print_another = 'y'
while print_another == 'y':
    
    # Ask user for input
    cruiser_name = input('Enter passenger name: ')
    cruiser_age = int(input('Enter passenger age: (input a whole number between 1 - 100) '))
    print()

    # Child Activities
    if cruiser_age >= 1 and cruiser_age <= 12:
        print('All children ages 12 and under can enjoy the following activities:')
        print('\tKids Club')
        print('\tSplash Zone')
        print()

    # Teenager Activities (13–17)
    elif cruiser_age >= 13 and cruiser_age <= 17:
        print('All teenagers ages 13-19 can enjoy the following activities:')
        print('\tTeen Club')
        print('\tWater Slides')
        print()

    # Teen + Young Adult (18–19)
    elif cruiser_age == 18 or cruiser_age == 19:
        print('All teenagers ages 13-19 can enjoy the following activities:')
        print('\tTeen Club')
        print('\tWater Slides')
        print('All 18 and 19 year old passengers may also participate in:')
        print('\tDance Club')
        print('\tComedy Club')
        print('\tAdult Pool')
        print()

    # Young Adult (age 20)
    elif cruiser_age == 20:
        print('All young adult passengers age 20 may enjoy the following activities:')
        print('\tDance Club')
        print('\tComedy Club')
        print('\tAdult Pool')
        print()

    # Adult (21–64)
    elif cruiser_age >= 21 and cruiser_age < 65:
        print('All adults 21 and older can enjoy the following activities:')
        print('\tDance Club')
        print('\tComedy Club')
        print('\tAdult Pool')
        print('\tAll bars and casinos')
        print('As a reminder, please drink responsibly!')
        print()
    
    elif cruiser_age <= 0 or cruiser_age >= 120:
        print('---INVALID AGE ENTERED---')
        print()

    # Senior (65+)
    else:
        print('All adults 21 and older can enjoy the following activities:')
        print('\tDance Club')
        print('\tComedy Club')
        print('\tAdult Pool')
        print('\tAll bars and casinos')
        print('Senior cruisers are entitled to a 15% purchase discount on-board')
        print('As a reminder, please drink responsibly!')
        print()

    print_another = input('Would you like to print another activity list for a new passenger? y or n? ')
    print()

print("Enjoy your cruise!")