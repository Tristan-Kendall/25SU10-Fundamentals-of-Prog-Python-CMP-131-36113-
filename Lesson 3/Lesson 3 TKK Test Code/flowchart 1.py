# prompt the user
first_color  = input('Enter the first color: ')
second_color = input('Enter the second color: ')

# allowed input
valid = ('red', 'orange', 'yellow', 'green', 'blue', 'purple')

# validation
if first_color not in valid or second_color not in valid:
    print('You did not enter one of red, orange, yellow, green, blue or purple')

# complementary check
elif (first_color == 'red' and second_color == 'green') or \
    (first_color == 'green' and second_color == 'red') or \
    (first_color == 'yellow' and second_color == 'purple') or \
    (first_color == 'purple' and second_color == 'yellow') or \
    (first_color == 'blue' and second_color == 'orange') or \
    (first_color == 'orange' and second_color == 'blue'):
    print('The two colors are complementary')

# everything else
else:
    print('The two colors are not complementary')
