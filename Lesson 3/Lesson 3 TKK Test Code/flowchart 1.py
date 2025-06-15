#declaring colors
first_color = 'red' or 'yellow' or 'blue'
second_color = 'green' or 'purple' or 'orange'

#prompt user for input
first_color = print(str(input('Enter the first color:')))
second_color = print(str(input('Enter the second color:')))

#if user selected the wrong color:
if first_color != ('red', 'green', 'yellow'):
    print('You did not enter one of red, orange, yellow, green, blue, or purple1')

if second_color != ('purple', 'blue', 'orange'):
    print('You did not enter one of red, orange, yellow, green, blue, or purple2')

#if user selected the correct color:
elif ('red' or 'yellow' or 'blue' and 'green' or 'purple' or 'orange'):
    print('The two colors are complementary')

#this does not work as a result, I'm trying to figure out a more effecient way of doing this. I paused.