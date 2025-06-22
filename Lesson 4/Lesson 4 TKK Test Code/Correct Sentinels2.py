# Assume the variable right_value has already been assigned an integer between 0 and 100, This is the number the user must guess
# Assigning a random number to right_value
right_value = 27

# creating simple counter for guess count
guess_value = 0

while True:
    user_input = int(input('Enter a guess: '))
    guess_value += 1

    if user_input < right_value:
        print('Your guess is too low.')
    elif user_input < right_value:
        print('Your guess is too high.')
    else:
        print(f'Correct! it took you {guess_value} guesses.')