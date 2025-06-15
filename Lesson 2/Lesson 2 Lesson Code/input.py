# Get the user's name, age, and income.
name = input('What is your name? ')
age = int(input('What is your age? '))
income = float(input('What is your income? '))

# Display the data.
print('Here is the data you entered:')
print('Name:', name)
print('Age:', age)
print('Income:', income)

# Calculating the user's age & salary in 5 years, then displaying it.
print('In 5 years you will be:', age+5)
print('Hopefully you will earn:', income+40000, "a year!")