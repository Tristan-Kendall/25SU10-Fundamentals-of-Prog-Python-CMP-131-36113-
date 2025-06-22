number = 0

# Keep prompting until a valid number is entered
while number < 1 or number > 100:
    number = int(input('Enter a number from 1 through 100: '))

# Display the multiplication table
for i in range(1, 11):
    print(f'{number} x {i} = {number * i}')
