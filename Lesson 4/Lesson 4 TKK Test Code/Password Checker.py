# Asking the user for input
enter_pass = str(input('Enter the password:'))

# Storing our correct password as a string
correct_pass = str('python123')
# Creating the counter
invalid_attempt_counter = int(0)

# The looper
while enter_pass != correct_pass:
    invalid_attempt_counter += 1
    enter_pass = str(input("Wrong password. Try again: "))
print(f'Number of invalid attempts: {invalid_attempt_counter}')
print("Access Granted!")
