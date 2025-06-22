# Assume the variable right_value has already been assigned an integer between 0 and 100, This is the number the user must guess
# Assigning a random number to right_value
right_value = 27

user_input = int(input('Enter a guess:'))
guess_value = 0

# user's input is too low
while right_value > user_input:
    user_input = int(input('Your guess is too low.'))
    guess_value += 1

# user's input is too high
while right_value < user_input:
    user_input = int(input('Your guess is too high.'))
    guess_value += 1

# user enters the correct value.
if user_input == right_value:
    print(f'Correct! It took you {guess_value} guesses.')